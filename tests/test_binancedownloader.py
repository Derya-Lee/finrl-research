import pytest
from finrl.meta.preprocessor.binancedownloader import BinanceDownloader

def test_download_ohlcv_returns_dataframe():
    downloader = BinanceDownloader()
    df = downloader.download_ohlcv("BTCUSDT", start_str="1 Jan, 2023", end_str="10 Jan, 2023")
    
    assert not df.empty, "Returned DataFrame is empty"
    assert set(["date", "open", "high", "low", "close", "volume", "tic"]).issubset(df.columns), "Missing expected columns"
    assert df["tic"].iloc[0] == "BTC-USD"

def test_download_multiple_returns_combined_df():
    downloader = BinanceDownloader()
    df = downloader.download_multiple(["BTCUSDT", "ETHUSDT"], start_str="1 Jan, 2023", end_str="5 Jan, 2023")

    assert not df.empty
    assert df["tic"].nunique() == 2
    assert "ETH-USD" in df["tic"].values
    assert "BTC-USD" in df["tic"].values
