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
    def DRL_evaluation(model, environment):
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

        result = compute_sharpe_metrics(account_memory)
        return result

            # if step_counter < 5 or step_counter >= max_steps - 5:
            #     print(f"{'[TRADE]' if not evaluate else '[VALIDATION]'} Step {step_counter + 1} | "f"Reward (scaled): {reward} | Asset: {total_asset:,.2f}")
    
    @staticmethod
    def DRL_prediction(model, environment, start_date):
        obs = environment.reset()
        total_asset = environment.envs[0].cash  # should be 1,000,000
        done = False
        total_reward = 0
        daily_records = []  # store daily metrics      
        daily_records.append({
            "date": start_date,
            "account_value": total_asset,
            "reward": 0.0,
            "daily_volatility": 0.0,
            "trade_count": 0
        })

        while not done:
            action, _ = model.predict(obs)
            obs, reward, done, _ = environment.step(action)

            env_inst = environment.envs[0]
            date_today = env_inst.data.date.iloc[0]
            trade_count = getattr(env_inst, "trade_count", 0) 
            total_asset = env_inst.total_asset
            total_reward += float(reward)

 
            # Simple volatility for the day (based on price change)
            prices_today = env_inst.data.close.values
            vol_today = np.std(prices_today) if len(prices_today) > 1 else 0

            if not done:
                # account_memory.append(total_asset)
                daily_records.append({
                    "date": date_today,
                    "account_value": total_asset,
                    "reward": float(reward),
                    "daily_volatility": vol_today,
                    "trade_count": trade_count
                })


        df_daily = pd.DataFrame(daily_records)

        return df_daily
