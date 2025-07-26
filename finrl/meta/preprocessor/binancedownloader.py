from binance.client import Client
import pandas as pd
import time

class BinanceDownloader:
    def __init__(self):
        self.client = Client()  # No API key needed for historical data

    def download_ohlcv(self, symbol="BTCUSDT", interval="1d", start_str="1 Jan, 2018", end_str=None):
        klines = self.client.get_historical_klines(symbol, interval, start_str, end_str)

        df = pd.DataFrame(klines, columns=[
            "timestamp", "open", "high", "low", "close", "volume",
            "close_time", "quote_asset_volume", "num_trades",
            "taker_buy_base", "taker_buy_quote", "ignore"
        ])
        # df['date'] = pd.to_datetime(df['date']) ?
        df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
        df["tic"] = symbol.replace("USDT", "-USD")
        df = df[["date", "open", "high", "low", "close", "volume", "tic"]]
        df = df.astype({"open": float, "high": float, "low": float, "close": float, "volume": float})
        return df

    def download_multiple(self, ticker_list, interval="1d", start_str="1 Jan, 2018", end_str=None):
        df_list = [self.download_ohlcv(ticker, interval, start_str, end_str) for ticker in ticker_list]
        df_all = pd.concat(df_list, ignore_index=True).sort_values(["date", "tic"]).dropna()
        return df_all
