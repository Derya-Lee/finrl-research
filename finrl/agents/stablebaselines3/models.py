# DRL models from Stable Baselines 3
from __future__ import annotations

import statistics
import time

import numpy as np
import pandas as pd
# from stable_baselines3 import A2C
from stable_baselines3 import DDPG
# from stable_baselines3 import PPO
from stable_baselines3 import SAC
from stable_baselines3 import TD3
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.callbacks import CallbackList
from stable_baselines3.common.noise import NormalActionNoise
from stable_baselines3.common.noise import OrnsteinUhlenbeckActionNoise
from stable_baselines3.common.vec_env import DummyVecEnv

from finrl import config
from finrl.meta.env_stock_trading.env_stocktrading import StockTradingEnv
from finrl.meta.preprocessor.preprocessors import data_split

MODELS = {"ddpg": DDPG, "td3": TD3, "sac": SAC}

MODEL_KWARGS = {x: config.__dict__[f"{x.upper()}_PARAMS"] for x in MODELS.keys()}

NOISE = {
    "normal": NormalActionNoise,
    "ornstein_uhlenbeck": OrnsteinUhlenbeckActionNoise,
}


class TensorboardCallback(BaseCallback):
    """
    Custom callback for plotting additional values in tensorboard.
    """

    def __init__(self, verbose=0):
        super().__init__(verbose)

    def _on_step(self) -> bool:
        try:
            self.logger.record(key="train/reward", value=self.locals["rewards"][0])

        except BaseException as error:
            try:
                self.logger.record(key="train/reward", value=self.locals["reward"][0])

            except BaseException as inner_error:
                # Handle the case where neither "rewards" nor "reward" is found
                self.logger.record(key="train/reward", value=None)
                # Print the original error and the inner error for debugging
                print("Original Error:", error)
                print("Inner Error:", inner_error)
        return True

    def _on_rollout_end(self) -> bool:
        try:
            rollout_buffer_rewards = self.locals["rollout_buffer"].rewards.flatten()
            self.logger.record(
                key="train/reward_min", value=min(rollout_buffer_rewards)
            )
            self.logger.record(
                key="train/reward_mean", value=statistics.mean(rollout_buffer_rewards)
            )
            self.logger.record(
                key="train/reward_max", value=max(rollout_buffer_rewards)
            )
        except BaseException as error:
            # Handle the case where "rewards" is not found
            self.logger.record(key="train/reward_min", value=None)
            self.logger.record(key="train/reward_mean", value=None)
            self.logger.record(key="train/reward_max", value=None)
            print("Logging Error:", error)
        return True


class DRLAgent:
    """Provides implementations for DRL algorithms

    Attributes
    ----------
        env: gym environment class
            user-defined class

    Methods
    -------
        get_model()
            setup DRL algorithms
        train_model()
            train DRL algorithms in a train dataset
            and output the trained model
        DRL_prediction()
            make a prediction in a test dataset and get results
    """

    def __init__(self, env):
        self.env = env

    def get_model(
        self,
        model_name,
        policy="MlpPolicy",
        policy_kwargs=None,
        model_kwargs=None,
        verbose=1,
        seed=None,
        tensorboard_log=None,
    ):
        model_name = model_name.lower()
        if model_name not in MODELS:
            raise ValueError(
                f"Model '{model_name}' not found in MODELS."
            )  # this is more informative than NotImplementedError("NotImplementedError")

        if model_kwargs is None:
         
            model_kwargs = MODEL_KWARGS[model_name]

        if "action_noise" in model_kwargs:
            n_actions = self.env.action_space.shape[-1]
            model_kwargs["action_noise"] = NOISE[model_kwargs["action_noise"]](
                mean=np.zeros(n_actions), sigma=0.1 * np.ones(n_actions)
            )
        print(model_kwargs)
        return MODELS[model_name](
            policy=policy,
            env=self.env,
            tensorboard_log=tensorboard_log,
            verbose=verbose,
            policy_kwargs=policy_kwargs,
            seed=seed,
            **model_kwargs,
        )

    @staticmethod
    def train_model(
        model,
        model_name,
        tb_log_name,
        iter_num,
        total_timesteps=5000,
        callbacks: Type[BaseCallback] = None,
    ):
        model = model.learn(
            total_timesteps=total_timesteps,
            tb_log_name=tb_log_name,
            callback=(
                CallbackList(
                    [TensorboardCallback()] + [callback for callback in callbacks]
                )
                if callbacks is not None
                else TensorboardCallback()
            ),
        )
        model.save(
            f"{config.TRAINED_MODEL_DIR}/{model_name.upper()}_{total_timesteps // 1000}k_{iter_num}"
        )
        # assert os.path.exists(model_path), f"Model {model_name} failed to save!"
        return model

    @staticmethod
    def DRL_prediction(model, environment, deterministic=True):
        """make a prediction and get results"""
        test_env, test_obs = environment.get_sb_env()
        account_memory = None  # This help avoid unnecessary list creation
        actions_memory = None  # optimize memory consumption
        # state_memory=[] #add memory pool to store states

        test_env.reset()
        max_steps = len(environment.df.index.unique()) - 1

        for i in range(len(environment.df.index.unique())):
            action, _states = model.predict(test_obs, deterministic=deterministic)
            # account_memory = test_env.env_method(method_name="save_asset_memory")
            # actions_memory = test_env.env_method(method_name="save_action_memory")
            test_obs, rewards, dones, info = test_env.step(action)

            if (
                i == max_steps - 1
            ):  # more descriptive condition for early termination to clarify the logic
                account_memory = test_env.env_method(method_name="save_asset_memory")
                actions_memory = test_env.env_method(method_name="save_action_memory")
            # add current state to state memory
            # state_memory=test_env.env_method(method_name="save_state_memory")

            if dones[0]:
                print("hit end!")
                break
        return account_memory[0], actions_memory[0]

    # TODO: Check why not used
    @staticmethod
    def DRL_prediction_load_from_file(model_name, environment, cwd, deterministic=True):
        if model_name not in MODELS:
            raise ValueError(
                f"Model '{model_name}' not found in MODELS."
            )  # this is more informative than NotImplementedError("NotImplementedError")
        try:
            # load agent
            model = MODELS[model_name].load(cwd)
            print("Successfully load model", cwd)
        except BaseException as error:
            raise ValueError(f"Failed to load agent. Error: {str(error)}") from error

        # test on the testing env
        state = environment.reset()
        episode_returns = []  # the cumulative_return / initial_account
        episode_total_assets = [environment.initial_total_asset]
        done = False
        while not done:
            action = model.predict(state, deterministic=deterministic)[0]
            state, reward, done, _ = environment.step(action)

            total_asset = (
                environment.amount
                + (environment.price_ary[environment.day] * environment.stocks).sum()
            )
            episode_total_assets.append(total_asset)
            episode_return = total_asset / environment.initial_total_asset
            episode_returns.append(episode_return)

        print("episode_return", episode_return)
        print("Test Finished!")
        return episode_total_assets


class DRLEnsembleAgent:
    def __init__(self, df, train_period, val_test_period, rebalance_window, validation_window, env_kwargs):      
        self.df = df
        self.train_period = train_period
        self.val_test_period = val_test_period
        self.env_kwargs = env_kwargs
        self.unique_trade_date = df[
            (df.date > val_test_period[0]) & (df.date <= val_test_period[1])
        ].date.unique()
        self.rebalance_window = rebalance_window
        self.validation_window = validation_window
        self.train_env = None  # will be set externally later if needed


        self.env = DummyVecEnv([
            lambda: StockTradingEnv(
                df=df[(df.date >= train_period[0]) & (df.date <= train_period[1])],
                num_stock_shares=[0] * env_kwargs["stock_dim"],
                **env_kwargs
            )
        ])

    def _get_train_val_windows(self):
        start_day = self._get_day_from_date(self.train_period[0])
        end_day = self._get_day_from_date(self.val_test_period[1])
        max_day = self.df['day'].max()
        total_window = self.rebalance_window + self.validation_window

        latest_start_day = max_day - total_window

        train_val_windows = []

        for i in range(start_day, latest_start_day + 1, self.rebalance_window):
            train_start = i
            train_end = i + self.rebalance_window
            val_start = train_end
            val_end = val_start + self.validation_window

            if val_end > max_day:
                print(f"[INFO] Skipping window starting at day {i} (val_end={val_end} > max_day={max_day})")
                break

            train_data = self.df[(self.df['day'] >= train_start) & (self.df['day'] < train_end)]
            val_data = self.df[(self.df['day'] >= val_start) & (self.df['day'] < val_end)]

            train_val_windows.append((train_data, val_data, train_start, train_end, val_start, val_end))

            return train_val_windows

    @staticmethod
    def train_model(
        model,
        tb_log_name,
        total_timesteps=5000,
        callbacks: Type[BaseCallback] = None,
    ):  # this function is static method, so it can be called without creating an instance of the class
        model = model.learn(
            total_timesteps=total_timesteps,
            tb_log_name=tb_log_name,
            callback=(
                CallbackList(
                    [TensorboardCallback()] + [callback for callback in callbacks]
                )
                if callbacks is not None
                else TensorboardCallback()
            ),
        )
        return model


    @staticmethod
    def get_validation_sharpe(iteration, model_name):
        """Calculate Sharpe ratio based on validation results"""
        df_total_value = pd.read_csv(
            f"results/account_value_validation_{model_name}_{iteration}.csv"
        )
        # If the agent did not make any transaction
        if df_total_value["daily_return"].var() == 0:
            if df_total_value["daily_return"].mean() > 0:
                return np.inf
            else:
                return 0.0
        else:
            return (
                (4**0.5)
                * df_total_value["daily_return"].mean()
                / df_total_value["daily_return"].std()
            )

    def DRL_validation(self, model, test_data, test_env, test_obs):
        """validation process"""
        for _ in range(len(test_data.index.unique())):
            action, _states = model.predict(test_obs)
            test_obs, rewards, dones, info = test_env.step(action)

    def DRL_prediction(
        self, model, name, last_state, iter_num, turbulence_threshold, initial
    ):
        """make a prediction based on trained model"""

        # trading env
        trade_data = data_split(
            self.df,
            start=self.unique_trade_date[iter_num - self.rebalance_window],
            end=self.unique_trade_date[iter_num],
        )

        # trade_env = DummyVecEnv(
        #     [
        #         lambda: StockTradingEnv(
        #             df=trade_data,                        # override
        #             mode="trade",                         # override
        #             model_name=name,                      # override
        #             iteration=iter_num,                   # override
        #             initial=initial,                      # override
        #             previous_state=last_state,            # override
        #             turbulence_threshold=turbulence_threshold,  # override
        #             print_verbosity=self.env_kwargs["print_verbosity"],       # override
        #             **self.env_kwargs                     # all other static/shared parameters
        #         )
        #     ]
        # )
        trade_obs = trade_env.reset()

        for i in range(len(trade_data.index.unique())):
            action, _states = model.predict(trade_obs)
            trade_obs, rewards, dones, info = trade_env.step(action)
            if i == (len(trade_data.index.unique()) - 2):
                # print(env_test.render())
                last_state = trade_env.envs[0].render()

        df_last_state = pd.DataFrame({"last_state": last_state})
        df_last_state.to_csv(f"results/last_state_{name}_{i}.csv", index=False)
        return last_state

    def _train_window(
        self,
        model_name,
        model_kwargs,
        sharpe_list,
        validation_start_date,
        validation_end_date,
        timesteps_dict,
        i,
        train,
        validation,
        turbulence_threshold
    ):
        stock_dimension = self.env_kwargs["stock_dim"]
        train_env = DummyVecEnv([
            lambda: StockTradingEnv(
                df=train,
                mode="train",
                model_name=model_name,
                iteration=i,
                num_stock_shares=[0] * stock_dimension,
                **self.env_kwargs
            )
        ])

        model = self.get_model(model_name, train_env, policy="MlpPolicy", model_kwargs=model_kwargs)

        model = self.train_model(
            model=model,
            model_name=model_name,
            tb_log_name=model_name,
            total_timesteps=timesteps_dict[model_name],
        )

        val_env = DummyVecEnv([
            lambda: StockTradingEnv(
                df=validation,
                mode="validation",
                model_name=model_name,
                iteration=i,
                num_stock_shares=[0] * stock_dimension,
                **self.env_kwargs
            )
        ])

        val_obs = val_env.reset()

        sharpe = self.DRL_validation(
            model=model,
            test_data=validation,
            test_env=val_env,
            test_obs=val_obs,
        )

        sharpe_list.append(sharpe)

        return model, sharpe_list, sharpe


    def run_ensemble_strategy(
        self,
        DDPG_model_kwargs=None,
        SAC_model_kwargs=None,
        TD3_model_kwargs=None,
        timesteps_dict=None
    ):
        model_kwargs_dict = {
            "DDPG": DDPG_model_kwargs,
            "SAC": SAC_model_kwargs,
            "TD3": TD3_model_kwargs,
        }
        
        assert timesteps_dict is not None, "You must provide timesteps_dict"

        total_window = self.rebalance_window + self.validation_window
        start = self._get_day_from_date(self.train_period[0])
        max_valid_day = self.df['day'].max()
        latest_start = max_valid_day - total_window

        model_dct = {
            k.lower(): {"sharpe_list": [], "model_path": None, "sharpe": None}
            for k in model_kwargs_dict if model_kwargs_dict[k] is not None
        }

        for i in range(start, latest_start + 1, self.rebalance_window):
            train_start = i
            train_end = i + self.rebalance_window
            val_start = train_end
            val_end = val_start + self.validation_window

            if val_end > max_valid_day:
                print(f"[INFO] Skipping window starting at day {i} (val_end={val_end} > max_day={max_valid_day})")
                break

            for model_name_raw, kwargs in model_kwargs_dict.items():
                if kwargs is None:
                    continue
                    
                print(f"======{model_name} Training========")

                model_name = model_name_raw.lower()
                train_data = self.df[(self.df.day >= train_start) & (self.df.day < train_end)]
                val_data = self.df[(self.df.day >= val_start) & (self.df.day < val_end)]

                trained_model, sharpe_list, sharpe = self._train_window(
                    model_name=model_name,
                    model_kwargs=kwargs,
                    sharpe_list=model_dct[model_name]["sharpe_list"],
                    validation_start_date=val_start,
                    validation_end_date=val_end,
                    timesteps_dict=timesteps_dict,
                    i=i,
                    train=train_data,
                    validation=val_data,
                    turbulence_threshold=self.env_kwargs.get("turbulence_threshold", None),
                )
                model_dct[model_name]["sharpe_list"] = sharpe_list
                model_dct[model_name]["sharpe"] = sharpe
                model_dct[model_name]["model_path"] = getattr(trained_model, "model_path", None)

        return pd.DataFrame({
            "Model": list(model_dct.keys()),
            "Sharpe": [model_dct[k]["sharpe"] for k in model_dct]
        })
