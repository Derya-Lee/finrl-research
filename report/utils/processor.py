import os
import pandas as pd
import numpy as np
import sys

sys.path.append("..")
from pathlib import Path

class ProcessTools:
    
    @staticmethod
    def compute_sortino_ratio(daily_df, risk_free=0.0):
        """Compute Sortino ratio for one window dataframe"""
        returns = daily_df["account_value"].pct_change().dropna().astype(float)
        if returns.empty:
            return np.nan
        excess = returns - float(risk_free)

        # Downside returns only
        downside = excess[excess < 0]
        if downside.std() == 0 or downside.empty:
            return np.nan

        return np.sqrt(365) * excess.mean() / downside.std()

    @staticmethod
    def compute_sharpe_ratio(daily_df, risk_free=0.0):
        """Compute Sharpe ratio for one window dataframe"""
        returns = daily_df["account_value"].pct_change().dropna().astype(float)
        if returns.empty:
            return np.nan
        excess = returns - float(risk_free)
        return np.sqrt(365) * excess.mean() / excess.std() if excess.std() > 0 else np.nan

    @staticmethod
    def summarize_window(daily_df, window, agents_array, features_used="none"):
        """Summarize one window of results"""

        initial_capital = 1000000
        # Remove first row (initial capital entry) if in account_values:
        # daily_df = daily_df.iloc[1:].reset_index(drop=True)

        sharpe = ProcessTools.compute_sharpe_ratio(daily_df)
        avg_account_value = daily_df["account_value"].mean()
        final_account_value = daily_df["account_value"].iloc[-1]

        sortino = ProcessTools.compute_sortino_ratio(daily_df)
        profit_loss = final_account_value - initial_capital
        avg_reward = daily_df["reward"].mean()
        max_drawdown = (daily_df["account_value"].cummax() - daily_df["account_value"]).max()
        
        chosen_agent = agents_array[window - 1]  # window starts at 1

        return {
            "window": window,
            "agent": chosen_agent,
            "sharpe": sharpe,
            "sortino": sortino,
            "avg_account_value": avg_account_value,
            "final_account_value": final_account_value,
            "profit_loss": profit_loss,
            "avg_daily_reward": avg_reward,
            "max_drawdown": max_drawdown,
            "features_used": features_used
        }