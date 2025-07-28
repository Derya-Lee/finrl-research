import os
import numpy as np
import pandas as pd
from stable_baselines3 import A2C, PPO, DDPG
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.noise import NormalActionNoise

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
    def DRL_prediction(model, environment, evaluate=False):
        obs = environment.reset()
        account_memory = []

        step_counter = 0
        while True:
            action, _states = model.predict(obs)
            obs, reward, done, info = environment.step(action)

            total_asset = environment.envs[0].total_asset  # tracked inside env
            account_memory.append(total_asset)

            # Print debug for first 5 and last 5 steps only
            if step_counter < 5 or done:
                print(f" Step {step_counter + 1} | Asset: {total_asset:,.2f}")
            step_counter += 1

            if done:
                break

        # EVALUATE MODE — SHARPE CALCULATION
        if evaluate:
            if len(account_memory) < 2:
                print(" Not enough data to calculate Sharpe ratio.")
                return float('nan')

            daily_returns = pd.Series(account_memory).pct_change().dropna()

            if daily_returns.std() == 0 or daily_returns.empty:
                print(" Sharpe Debug: No volatility or insufficient data.")
                return float('nan')

            sharpe = (252**0.5) * daily_returns.mean() / daily_returns.std()
            print(" Sharpe Debug:")
            print(f"   Mean return: {daily_returns.mean():.5f}")
            print(f"   Std return : {daily_returns.std():.5f}")
            print(f"   Sharpe     : {sharpe:.5f}")
            return sharpe

        # PREDICTION MODE — RETURN FULL ACCOUNT VALUE DATAFRAME
        else:
            df_result = pd.DataFrame({
                'date': range(len(account_memory)),
                'account_value': account_memory
            })
            return df_result


