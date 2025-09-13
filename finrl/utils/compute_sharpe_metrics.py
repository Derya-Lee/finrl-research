import numpy as np
import pandas as pd

 # sharp: risk-adjusted return
def compute_sharpe_metrics(account_values, TRADING_DAYS_PER_YEAR = 365):  
    # Takes account_memory (series of total asset values).
    # Converts to daily returns with .pct_change().
    # Computes Sharpe ratio on those returns, annualized with 365

    daily_returns = pd.Series(account_values).pct_change().dropna()
    if daily_returns.empty:
        return {
                "mean_return": np.nan,
                "std_return": np.nan,
                "sharpe": np.nan,
                "daily_return_days": 0,
                "account_values": account_values,
                "daily_returns": []
            }
    
    if daily_returns.std() == 0 or daily_returns.empty:
        print("[EVAL] Sharpe Debug: No volatility or insufficient data.")
        
    mean_return = daily_returns.mean()
    std_return = daily_returns.std()
    sharpe = (TRADING_DAYS_PER_YEAR**0.5) * mean_return / std_return if std_return != 0 else np.nan

    return {
        "mean_return": mean_return,
        "std_return": std_return,
        "sharpe": sharpe,
        "daily_return_days": len(daily_returns),
        "account_values": account_values,
        "daily_returns": daily_returns.tolist()
    }
