import requests
import pandas as pd

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
