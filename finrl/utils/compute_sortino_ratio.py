import numpy as np
import pandas as pd

def compute_sortino_ratio(account_values, risk_free=0.0):
    """Compute Sortino ratio for one window dataframe"""

    daily_returns = pd.Series(account_values).pct_change().dropna().astype(float)
    if daily_returns.empty:
        return np.nan
    excess = daily_returns - float(risk_free)

    # Downside daily_returns only
    downside = excess[excess < 0]
    if downside.std() == 0 or downside.empty:
        return np.nan

    return np.sqrt(365) * excess.mean() / downside.std()

#    def compute_sortino_ratio(account_values, risk_free=0.0):
#     returns = pd.Series(account_values).pct_change().dropna().astype(float)
#     downside = returns[returns < 0].std()
#     if downside == 0 or returns.empty:
#         return np.nan
#     mean_excess = returns.mean() - risk_free/365
#     return (mean_excess * (365**0.5)) / downside
