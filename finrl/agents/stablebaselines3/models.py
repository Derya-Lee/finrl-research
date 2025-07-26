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
        while True:
            action, _states = model.predict(obs)
            obs, reward, done, info = environment.step(action)
            if done:
                break

        if evaluate:
            df_account_value = environment.envs[0].save_asset_memory()
            daily_returns = df_account_value["account_value"].pct_change().dropna()

            mean_return = daily_returns.mean()
            std_return = daily_returns.std()
            sharpe = (252 ** 0.5) * mean_return / std_return if std_return != 0 else np.nan

            print(f"\n📊 Sharpe Debug:")
            print(f"  ➤ Mean return: {mean_return:.6f}")
            print(f"  ➤ Std return : {std_return:.6f}")
            print(f"  ➤ Sharpe     : {sharpe:.3f}")

            return sharpe
        else:
            df_result = environment.envs[0].save_asset_memory()
            return df_result

