import numpy as np
import pandas as pd


def compute_sharpe_metrics(account_memory, TRADING_DAYS_PER_YEAR = 365):  
    if len(account_memory) < 2:
        #  print("[EVAL] Not enough data to calculate Sharpe ratio.")
        return {
            "mean_return": np.nan,
            "std_return": np.nan,
            "sharpe": np.nan,
            "daily_return_days": 0,
            "account_memory": account_memory,
            "daily_returns": []
        }

    daily_returns = pd.Series(account_memory).pct_change().dropna()
    
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
        "account_memory": account_memory,
        "daily_returns": daily_returns.tolist()
    }

# TODO add annualized_volatility = daily_returns.std() * np.sqrt(252)