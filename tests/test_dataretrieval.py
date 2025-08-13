
import sys
import os
import pandas as pd
import numpy as np
import pytest
from stable_baselines3.common.vec_env import DummyVecEnv
from finrl.agents.stablebaselines3.models import DRLAgent
from finrl.meta.env_crypto_trading.env_cryptotrading import CryptoTradingEnv
from finrl.meta.preprocessor.preprocessors import FeatureEngineer
from finrl.config import TRAIN_START_DATE, TRAIN_END_DATE
from finrl.meta.preprocessor.binancedownloader import BinanceDownloader
from stable_baselines3 import PPO

# Run with PYTHONPATH=. pytest tests/test_env_pipeline.py
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# sys.path.append("..")


# ---------- CONFIG ----------
tickers = ['BTC-USD', 'ETH-USD']
start_date = TRAIN_START_DATE
end_date = TRAIN_END_DATE

@pytest.fixture(scope="module")
def downloaded_data():
    downloader = BinanceDownloader()
    df_raw = downloader.download_multiple(ticker_list=["BTCUSDT", "ETHUSDT"], start_str="1 Jan, 2018")
    return df_raw

def test_raw_binance_data(downloaded_data):
    df = downloaded_data
    # unique_days = downloaded_data["date"].nunique()
    # print(f"📅 Unique trading days: {unique_days}")
    assert not df.empty, "❌ Raw data is empty"
    assert df["date"].is_monotonic_increasing, "❌ Dates are not sorted"
    assert df["close"].nunique() > 10, "❌ Close price has too few unique values"
    assert df.groupby("tic").size().min() > 30, "❌ Some tickers have too few rows"

    print("✅ Raw Binance data passes basic checks")
    print("Sample:", df.head())

def test_processed_data_indicators(downloaded_data):
    fe = FeatureEngineer(use_technical_indicator=True, tech_indicator_list=["macd", "rsi_30", "cci_30"])
    df = fe.preprocess_data(downloaded_data)
    assert "macd" in df.columns, "❌ MACD not in processed data"
    assert df["macd"].nunique() > 5, "❌ MACD has too few unique values"
    assert df.groupby("tic").size().min() > 30, "❌ Processed data too short for some tickers"
    
    print("✅ Processed data and indicators look valid")
    print(df[["date", "tic", "close", "macd"]].head())

def test_days_per_ticker(downloaded_data):
    for tic, group in downloaded_data.groupby("tic"):
        unique_days = group["date"].nunique()
        print(f"📈 {tic} has {unique_days} unique days")
        assert unique_days > 100, f"❌ {tic} has too few unique days"
    print("✅ All tickers have sufficient historical length")


def test_price_volatility(downloaded_data):
    for tic, group in downloaded_data.groupby("tic"):
        returns = group["close"].pct_change().dropna()
        std = returns.std()
        print(f"{tic} Volatility: {std:.5f}")
        assert std > 0.001, f"❌ {tic} has too low volatility for RL learning"
    
    print("✅ All tickers have non-zero volatility")