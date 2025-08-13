import pytest
from finrl.meta.env_crypto_trading.env_cryptotrading import CryptoTradingEnv
from finrl.agents.stablebaselines3.models import DRLAgent
from stable_baselines3.common.vec_env import DummyVecEnv
from pprint import pprint

def dummy_data():
    import pandas as pd
    import numpy as np
    dates = pd.date_range(start="2021-01-01", periods=5)
    df = pd.DataFrame({
        'date': dates.repeat(2),
        'tic': ['BTC-USD', 'ETH-USD'] * 5,
        'close': np.random.rand(10) * 10000,
        'macd': np.random.rand(10),
        'rsi_30': np.random.rand(10),
        'cci_30': np.random.rand(10),
    })
    return df

def test_reset_called_on_env_init():
    df = dummy_data()
    test_env = CryptoTradingEnv(df)
    assert test_env.reset_counter == 1, "❌ reset() should be called once during init"

def test_reset_called_on_prediction():
    df = dummy_data()
    test_env = DummyVecEnv([lambda: CryptoTradingEnv(df)])
    agent = DRLAgent(env=test_env)
    model = agent.train_PPO(total_timesteps=10)
    _ = DRLAgent.DRL_prediction(model=model, environment=test_env)

        # Remove the final day's asset value (no trade done)
    test_acc_vals = list(test_env.envs[0].asset_memory)
    # if len(test_acc_vals) > 1:
    #     test_acc_vals.pop()
    print(f" Account Value Range: {min(test_acc_vals)}, {max(test_acc_vals)})")
    print("****************")
    print(test_env)
    print("****************")
    pprint(test_env.envs[0].__dict__)

    assert test_env.envs[0].reset_counter >= 2, "❌ reset() should be called again during DRL_prediction"
