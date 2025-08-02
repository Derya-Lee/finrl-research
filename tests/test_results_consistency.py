
import sys
import os
import pandas as pd
import numpy as np
import pytest
from stable_baselines3.common.vec_env import DummyVecEnv
from finrl.agents.stablebaselines3.models import DRLAgent
from finrl.meta.env_crypto_trading.env_cryptotrading import CryptoTradingEnv
from finrl.meta.preprocessor.preprocessors import FeatureEngineer
# from finrl.config import TRAIN_START_DATE, TRAIN_END_DATE
from finrl.meta.preprocessor.binancedownloader import BinanceDownloader
from stable_baselines3 import PPO

def test_total_rewards_vs_account_change():
    # === Setup Dummy Data & Environment ===
    downloader = BinanceDownloader()
    df_raw = downloader.download_multiple(ticker_list=["BTCUSDT"], start_str="1 Jan, 2019", end_str="1 Jan, 2021")

    fe = FeatureEngineer(use_technical_indicator=True, tech_indicator_list=["macd", "rsi_30", "cci_30"])
    df_processed = fe.preprocess_data(df_raw)

    # Train window
    train_data = df_processed[(df_processed['date'] >= "2019-01-01") & (df_processed['date'] < "2021-01-01")]

    env = DummyVecEnv([lambda: CryptoTradingEnv(train_data)])
    agent = DRLAgent(env=env)
    model = agent.train_PPO(total_timesteps=1000)

    # === Run DRL prediction ===
    df_result = DRLAgent.DRL_prediction(model, env)
    final_val = df_result["account_value"].iloc[-1]

    # === Access reward history from the environment ===
    raw_env = env.envs[0]
    rewards = np.diff(raw_env.asset_memory) * (1.0 / raw_env.reward_scaling)
    total_reward = np.sum(rewards)

    net_asset_change = final_val - raw_env.initial_amount

    print(f" Final Account Value: {final_val:,.2f}")
    print(f" Sum of Step Rewards (scaled): {total_reward:,.2f}")
    print(f" Net Change in Account: {net_asset_change:,.2f}")

    # === Test Assertion (allow small numerical tolerance) ===
    assert abs(total_reward - net_asset_change) < 1e-3, "❌ Rewards and account delta mismatch"


def test_train_window_days_alignment():
    train_start = pd.to_datetime("2020-01-01")
    train_end = pd.to_datetime("2020-12-31")

    downloader = BinanceDownloader()
    df_raw = downloader.download_multiple(ticker_list=["BTCUSDT"], start_str="1 Jan, 2018")
    fe = FeatureEngineer(use_technical_indicator=True, tech_indicator_list=["macd", "rsi_30", "cci_30"])
    df_processed = fe.preprocess_data(df_raw)

    df_train = df_processed[(df_processed["date"] >= train_start) & (df_processed["date"] < train_end)]
    actual_days = df_train["date"].nunique()

    expected_days = len(pd.date_range(start=train_start, end=train_end, freq="D"))

    print(f"Expected trading days: {expected_days}")
    print(f"Actual unique days in train_data: {actual_days}")

    assert actual_days <= expected_days, "❌ More trading days than expected (check data filtering)"
    assert actual_days > 200, "❌ Too few training days"
