import os
import numpy as np
import pandas as pd
from stable_baselines3 import A2C, PPO, DDPG
from stable_baselines3.common.noise import NormalActionNoise
from port_DRL_exp.utils.compute_sharpe_metrics import compute_sharpe_metrics

class DRLAgent:
    def __init__(self, env):
        self.env = env

    def train_PPO(self, total_timesteps=10000, model_kwargs=None):
        model_kwargs = model_kwargs or {}
        # NOTE  replace verbose=1 to see training progress
        model = PPO('MlpPolicy', self.env, verbose=0, **model_kwargs)
        model.learn(total_timesteps=total_timesteps)
        return model

    def train_A2C(self, total_timesteps=10000, model_kwargs=None):
        model_kwargs = model_kwargs or {}
        model = A2C('MlpPolicy', self.env, verbose=0, **model_kwargs)
        model.learn(total_timesteps=total_timesteps)
        return model

    def train_DDPG(self, total_timesteps=10000, model_kwargs=None):
        model_kwargs = model_kwargs or {}
        n_actions = self.env.action_space.shape[0]
        action_noise = NormalActionNoise(mean=np.zeros(n_actions), sigma=0.1 * np.ones(n_actions))
        model = DDPG('MlpPolicy', self.env, action_noise=action_noise, verbose=0, **model_kwargs)
        model.learn(total_timesteps=total_timesteps)
        return model

    @staticmethod
    def DRL_evaluation(model, environment, lookback_days=0):
        obs = environment.reset()
        account_memory = []
        total_reward = 0
        done = False

        # obs = basic_state = [self.cash] + list(self.stocks) + prices.tolist()
        while not done:
            action, _ = model.predict(obs)
            obs, reward, done, _ = environment.step(action)
            total_reward += float(reward)
            total_asset = environment.envs[0].total_asset 
            account_memory.append(total_asset)

        account_memory_trimmed = account_memory[lookback_days:]

        result = compute_sharpe_metrics(account_memory_trimmed)
        return result


    @staticmethod
    def DRL_prediction(model, environment, start_date, lookback_days=0):
        obs = environment.reset()
        env_inst = environment.envs[0]
        total_asset = env_inst.total_asset
        #  total_asset = env_inst.cash : ignores any initial stock positions
        done = False
        total_reward = 0
        daily_records = []

        # Track how many days have passed since the start
        days_passed = 0

        # basic state
        initial_state = {
            "date": start_date,
            "account_value": total_asset,
            # "reward": 0.0,
            # "daily_return": 0.0,  
            "daily_volatility": 0.0,
        }
        # Add turbulence & volatility if env is featured
        if env_inst.featured:
            initial_state.update({
                "volatility": 0.0,
                "turbulence": 0.0,
            })

        # TODO check if to leave at all 0 - or are is the first record already ignored ( this is only for reporting )
        if env_inst.sentiment:
             initial_state.update({
                "fear_greed": -1,              # raw index (0–100)
                "fear_greed_norm": -1,    # normalized (0–1)
                "fear_greed_mapped": 0 # mapped (-2 … 2)
            })

        while not done:
            action, _ = model.predict(obs)

            # Force "hold" action during lookback period
            if days_passed < lookback_days:
                # print(f"lookback_days{lookback_days}")
                # print(f"days_passed{days_passed}")

                action = np.zeros_like(action)

            obs, reward, done, _ = environment.step(action)
            date_today = env_inst.data.date.iloc[0]
            # "environment doesn’t maintain a "total_asset" column" - "only close, tic, date, etc." explicitly computed total_asset:
            total_asset = env_inst.total_asset  
            total_reward += float(reward)

            # daily_returns = total_asset.pct_change().dropna()
            prices_today = env_inst.data.close.values
            # NOTE cross-sectional dispersion (cross-sectional daily price std) of prices “spread of asset prices per day,”
            vol_today = np.std(prices_today) if len(prices_today) > 1 else 0

            if not done:
                # Base record (always included)
                daily_record = {
                    "date": date_today,
                    "account_value": total_asset,
                    # "reward": float(reward),
                    # "daily_return": float(daily_returns),  
                    "daily_volatility": vol_today,
                }

                # Add turbulence & volatility if env is featured
                if env_inst.featured:
                    daily_record.update({
                        "volatility": env_inst.data["volatility"].iloc[0],  # eg. rolling 30-day
                        "turbulence": env_inst.data["turbulence"].iloc[0],
                    })

                if env_inst.sentiment:
                    daily_record.update({
                        "fear_greed": env_inst.data["fear_greed"].iloc[0],              # raw index (0–100)
                        "fear_greed_norm": env_inst.data["fear_greed_norm"].iloc[0],    # normalized (0–1)
                        "fear_greed_mapped": env_inst.data["fear_greed_mapped"].iloc[0] # mapped (-2 … 2)
                    })

                daily_records.append(daily_record)

            days_passed += 1

        df_daily = pd.DataFrame(daily_records)

        # print("------ df daily --------")
        # # print(type(df_daily.index))    
        # # print(df_daily.index[:5])  
        # # <class 'pandas.core.indexes.range.RangeIndex'>
        # print("------- END df daily --------")

        # Remove lookback days from results
        if lookback_days > 0:
            df_daily = df_daily.iloc[lookback_days:].reset_index(drop=True)


        # print(f"df_daily AFTER removed lookback days {len(df_daily)}")

        df_daily = pd.concat([pd.DataFrame([initial_state]), df_daily], ignore_index=True)

        return df_daily