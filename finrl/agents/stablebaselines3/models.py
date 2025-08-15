import os
import numpy as np
import pandas as pd
from stable_baselines3 import A2C, PPO, DDPG
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.noise import NormalActionNoise
from finrl.utils.compute_sharpe_metrics import compute_sharpe_metrics

class DRLAgent:
    def __init__(self, env):
        self.env = env

    def train_PPO(self, total_timesteps=10000, model_kwargs=None):
        model_kwargs = model_kwargs or {}
        # TODO temp replaced: model = PPO('MlpPolicy', self.env, verbose=0, **model_kwargs)
        model = PPO('MlpPolicy', self.env, verbose=1, **model_kwargs)
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


        while not done:
            action, _ = model.predict(obs)
            obs, reward, done, _ = environment.step(action)
            total_reward += float(reward)
            total_asset = environment.envs[0].total_asset 
            account_memory.append(total_asset)

        # lookback_days = environment.envs[0].lookback_days 
        account_memory_trimmed = account_memory[lookback_days:]

        result = compute_sharpe_metrics(account_memory_trimmed)
        return result


            # if step_counter < 5 or step_counter >= max_steps - 5:
            #     print(f"{'[TRADE]' if not evaluate else '[VALIDATION]'} Step {step_counter + 1} | "f"Reward (scaled): {reward} | Asset: {total_asset:,.2f}")

    @staticmethod
    def DRL_prediction(model, environment, start_date, lookback_days=0):
        obs = environment.reset()
        env_inst = environment.envs[0]
        total_asset = env_inst.cash  # should start at 1,000,000
        done = False
        total_reward = 0
        daily_records = []

        # Track how many days have passed since the start
        days_passed = 0

        # Record initial state
        initial_state = {
            "date": start_date,
            "account_value": total_asset,
            "reward": 0.0,
            "daily_volatility": 0.0,
            "trade_count": 0
        }

        while not done:
            action, _ = model.predict(obs)

            # Force "hold" action during lookback period
            if days_passed < lookback_days:
                print(f"lookback_days{lookback_days}")
                print(f"days_passed{days_passed}")

                action = np.zeros_like(action)

            obs, reward, done, _ = environment.step(action)
            date_today = env_inst.data.date.iloc[0]
            trade_count = getattr(env_inst, "trade_count", 0)
            total_asset = env_inst.total_asset
            total_reward += float(reward)

            prices_today = env_inst.data.close.values
            vol_today = np.std(prices_today) if len(prices_today) > 1 else 0

            if not done:
                daily_records.append({
                    "date": date_today,
                    "account_value": total_asset,
                    "reward": float(reward),
                    "daily_volatility": vol_today,
                    "trade_count": trade_count
                })

            days_passed += 1

        print(f"lookback_days{lookback_days}")
        print(f"days_passed{days_passed}")
        df_daily = pd.DataFrame(daily_records)

        # Remove lookback days from results
        if lookback_days > 0:
            df_daily = df_daily.iloc[lookback_days:].reset_index(drop=True)

        print(f"df_daily AFTER removed lookback days {len(df_daily)}")

        # first_real_date = df_daily["date"].iloc[0]
        # initial_state = {
        #     "date": first_real_date,
        #     "account_value": 1_000_000,
        #     "reward": 0.0,
        #     "daily_volatility": 0.0,
        #     "trade_count": 0
        # }
        df_daily = pd.concat([pd.DataFrame([initial_state]), df_daily], ignore_index=True)

        return df_daily




    # @staticmethod
    # def DRL_prediction(model, environment, start_date, lookback_days=0):
    #     obs = environment.reset()
    #     total_asset = environment.envs[0].cash  # should be 1,000,000
    #     done = False
    #     total_reward = 0
    #     daily_records = []  # store daily metrics      
    #     daily_records.append({
    #         "date": start_date,
    #         "account_value": total_asset,
    #         "reward": 0.0,
    #         "daily_volatility": 0.0,
    #         "trade_count": 0
    #     })

    #     while not done:
    #         action, _ = model.predict(obs)
    #         # ie. action = np.array([ 0.7, -0.3 ]) 
    #         # For asset 0 → buy 0.7 * hmax = 70 units
    #         # For asset 1 → sell 0.3 * hmax = 30 units
    #         obs, reward, done, _ = environment.step(action)

    #         env_inst = environment.envs[0]
    #         date_today = env_inst.data.date.iloc[0]
    #         trade_count = getattr(env_inst, "trade_count", 0) 
    #         total_asset = env_inst.total_asset
    #         total_reward += float(reward)
 
    #         prices_today = env_inst.data.close.values
    #         vol_today = np.std(prices_today) if len(prices_today) > 1 else 0

    #         if not done:
    #             daily_records.append({
    #                 "date": date_today,
    #                 "account_value": total_asset,
    #                 "reward": float(reward),
    #                 "daily_volatility": vol_today,
    #                 "trade_count": trade_count
    #             })

    #     df_daily = pd.DataFrame(daily_records)

    #     return df_daily

