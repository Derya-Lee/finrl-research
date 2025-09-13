import pandas as pd
import numpy as np
from finrl.config import LOOKBACK_DAYS

import pandas as pd
import numpy as np

# Min–max normalization : Squashes values to [0, 1]. "More stable for reinforcement learning"
import pandas as pd
import numpy as np

def add_turbulence_and_volatility(df, turbulence_lookback=LOOKBACK_DAYS, vol_lookback=30, normalization="minmax"):
    """
    Adds turbulence and rolling volatility columns to a price dataframe.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain columns ['date', 'tic', 'close'].
        'date' must be datetime64[ns].
    turbulence_lookback : int
        Lookback days for turbulence calculation.
    vol_lookback : int
        Lookback days for volatility calculation.
    normalization : str
        Either "minmax" (default) or "zscore" normalization for turbulence & volatility.

    Returns
    -------
    pd.DataFrame
        Original dataframe with 'turbulence' and 'volatility' columns added & normalized.
    """

    df = df.copy()

    # --- TURBULENCE ---
    price_pivot = df.pivot(index="date", columns="tic", values="close").pct_change()
    unique_dates = price_pivot.index

    turbulence_values = []
    for i in range(len(unique_dates)):
        if i < turbulence_lookback:
            turbulence_values.append(0)
            continue

        current_returns = price_pivot.iloc[i]
        hist_returns = price_pivot.iloc[i - turbulence_lookback:i]

        filtered_hist = hist_returns.dropna(axis=1)
        if filtered_hist.empty:
            turbulence_values.append(0)
            continue

        cov_matrix = filtered_hist.cov()
        mean_returns = filtered_hist.mean()

        diff = current_returns[filtered_hist.columns] - mean_returns
        try:
            turbulence = diff.values @ np.linalg.pinv(cov_matrix) @ diff.values.T
            turbulence_values.append(turbulence if turbulence > 0 else 0)
        except np.linalg.LinAlgError:
            turbulence_values.append(0)

    turbulence_df = pd.DataFrame({"date": unique_dates, "turbulence": turbulence_values})
    df = df.merge(turbulence_df, on="date", how="left")

    # --- VOLATILITY ---
    df['return'] = df.groupby('tic')['close'].pct_change()
    df['volatility'] = df.groupby('tic')['return'].rolling(vol_lookback).std().reset_index(0, drop=True)

    # Fill NaNs with 0 for early periods
    df['turbulence'] = df['turbulence'].fillna(0)
    df['volatility'] = df['volatility'].fillna(0)
    df = df.drop(columns=['return'])

    # --- NORMALIZATION ---
    if normalization == "minmax":
        # Normalize turbulence
        t_min, t_max = df['turbulence'].min(), df['turbulence'].max()
        df['turbulence'] = (df['turbulence'] - t_min) / (t_max - t_min + 1e-9)

        # Normalize volatility
        v_min, v_max = df['volatility'].min(), df['volatility'].max()
        df['volatility'] = (df['volatility'] - v_min) / (v_max - v_min + 1e-9)

    elif normalization == "zscore":
        # Z-score normalization
        df['turbulence'] = (df['turbulence'] - df['turbulence'].mean()) / (df['turbulence'].std() + 1e-9)
        df['volatility'] = (df['volatility'] - df['volatility'].mean()) / (df['volatility'].std() + 1e-9)

    return df


# -------------------------------------
# unused function: use for alternative volatility measures

def realized_volatility(df, lookback=30, price_col="close", group_col="tic"):
    # expects one row per tic/day; works per asset then merges back
    df = df.sort_values(["tic", "date"]).copy()
    df["ret"] = df.groupby(group_col)[price_col].pct_change()
    df["vol_"+str(lookback)] = (
        df.groupby(group_col)["ret"].rolling(window=lookback, min_periods=lookback).std().reset_index(level=0, drop=True)
    )
    return df.drop(columns=["ret"])

def ewma_volatility(df, span=30, price_col="close", group_col="tic"):
    df = df.sort_values(["tic", "date"]).copy()
    df["ret"] = df.groupby(group_col)[price_col].pct_change()
    df["ewm_vol_"+str(span)] = (
        df.groupby(group_col)["ret"].apply(lambda s: s.ewm(span=span, adjust=False).std())
    ).reset_index(level=0, drop=True)
    return df.drop(columns=["ret"])