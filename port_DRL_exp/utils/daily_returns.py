from copy import deepcopy
import pandas as pd

# currently not used, using finrl.plot version
def get_daily_return(df, value_col_name="account_value"):
    df = deepcopy(df)
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date")
    
    # Optional: Localize only if datetime is naive
    if df.index.tz is None:
        df.index = df.index.tz_localize("UTC")
    
    return df[value_col_name].pct_change().dropna()


# add df["cumulative_return"] = (1 + df["daily_return"]).cumprod()
# returns = get_daily_return(df_result)
# sharpe = (365**0.5) * returns.mean() / returns.std()