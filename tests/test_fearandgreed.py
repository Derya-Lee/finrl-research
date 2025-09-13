# from finrl.meta.preprocessor.preprocessors import FeatureEngineer
# or directly use :
# from finrl.utils import fear_and_greed

import requests
import os
import pandas as pd

# Tests appending fear & greed data through data processing.

def get_fear_greed(limit=0):
    """
    Fetch Crypto Fear & Greed index from alternative.me
    limit=0 returns all available history, otherwise last `limit` days.
    """
    url = f"https://api.alternative.me/fng/?limit={limit}&format=json"
    resp = requests.get(url).json()
    df = pd.DataFrame(resp["data"])

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    df = df.rename(columns={"value": "fear_greed"})
    df["fear_greed"] = df["fear_greed"].astype(int)

        # --- Normalized version (-1 to 1) ---
    df["fear_greed_norm"] = (df["fear_greed"] - 50) / 50.0

 # --- Mapped categorical version ---
    def map_fear_greed(value):
        if value <= 24:
            return -2   # extreme fear
        elif value <= 49:
            return -1   # fear
        elif value <= 74:
            return 1    # greed
        else:
            return 2    # extreme greed

    df["fear_greed_mapped"] = df["fear_greed"].apply(map_fear_greed)

    return df[["timestamp", "fear_greed", "fear_greed_norm", "fear_greed_mapped"]]

# copy from FeatureEngineer as modulenot found
def add_fear_greed(ohlcv_df):
 
    fng_df = get_fear_greed(limit=0)
    fng_df.rename(columns={"timestamp": "date"}, inplace=True)

    # ohlcv_df["date"] = pd.to_datetime(ohlcv_df["date"]).dt.normalize()
    fng_df["date"] = pd.to_datetime(fng_df["date"]).dt.normalize()


    # df = ohlcv_df.merge(fng_df[["date", "fear_greed", "fear_greed_norm", "fear_greed_mapped"]], on="date", how="left")
    # df["fear_greed"] = df["fear_greed"].fillna(method="ffill")


    # return df
    return fng_df

def test_fearandgreed():
    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, "data")
    results_path = os.path.join(current_dir, "results")
    file_name = "df-processed.csv"
    file_path = os.path.join(data_path, file_name)
    row_fg =  os.path.join(results_path, "daily_fear_greed.csv")
    # fe = FeatureEngineer(use_technical_indicator=False)

    
    ohlcv_df = pd.read_csv(file_path, parse_dates=["date"])

    fg_data = add_fear_greed(ohlcv_df)
    
    fg_data.to_csv(row_fg, index=False)
    # print(fg_data)

