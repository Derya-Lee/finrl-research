import pandas as pd
import numpy as np
import os

import sys

sys.path.append("..")
from pathlib import Path

from report.utils.processor import ProcessTools

current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, "data")

results_path = os.path.join(current_dir, "results")
os.makedirs(results_path, exist_ok=True)
results_file = os.path.join(results_path, "combined_summary.csv")

def generate_overview():


    phase_baseline_file = os.path.join(data_path, "account_values.csv")
    phase_turvol_file = os.path.join(data_path, "ft_account_values.csv")
    phase_sen_file = os.path.join(data_path, "sen_account_values.csv")




    phase1_baseline_df = pd.read_csv(phase_baseline_file, parse_dates=["date"])
    phase2_turvol_df = pd.read_csv(phase_turvol_file, parse_dates=["date"])
    phase3_sen_df = pd.read_csv(phase_sen_file, parse_dates=["date"])

    phase1_agents = ["DDPG", "DDPG", "PPO", "DDPG", "PPO", "PPO", "PPO", "PPO", "DDPG", "PPO", "DDPG", "A2C", "PPO", "DDPG", "A2C", "A2C", "DDPG", "PPO", "A2C", "DDPG", "PPO", "A2C", "A2C", "DDPG"]
    phase2_agents =["PPO", "PPO", "PPO", "PPO", "A2C", "DDPG", "A2C", "A2C", "A2C", "A2C", "A2C", "PPO", "PPO", "PPO", "A2C", "A2C", "PPO", "PPO", "PPO", "DDPG", "A2C", "A2C", "PPO", "A2C"]
    phase3_agents = ["PPO", "PPO", "DDPG", "DDPG", "PPO", "PPO", "PPO", "PPO", "A2C", "DDPG", "A2C", "DDPG", "PPO", "DDPG", "DDPG", "PPO", "DDPG", "A2C", "A2C", "A2C", "PPO", "DDPG", "PPO", "A2C"]


    results = []

    for window, daily_df in phase1_baseline_df.groupby("window"):
        # summary = pt.summarize_window(daily_df, window, phase1_agents, "Baseline")
        # results.append(summary)
        results.append(ProcessTools.summarize_window(daily_df, window, phase1_agents, "Baseline"))

    for window, daily_df in phase2_turvol_df.groupby("window"):
        # summary = pt.summarize_window(daily_df, window, phase2_agents, "Tur+Vol")
        # results.append(summary)
        results.append(ProcessTools.summarize_window(daily_df, window, phase2_agents, "Tur+Vol"))

    for window, daily_df in phase3_sen_df.groupby("window"):
        # summary = pt.summarize_window(daily_df, window, phase3_agents, "Sentiment")
        # results.append(summary)
        results.append(ProcessTools.summarize_window(daily_df, window, phase3_agents, "Sentiment"))

    df_results_summary = pd.DataFrame(results)
    df_results_summary.to_csv(results_file, index=False)
    print(f"Saved: {results_file}")

def describe_summary():
    df = pd.read_csv(results_file)

    # Average Sharpe by feature set
    print(df.groupby("features_used")["sharpe"].mean())

    # Average Sharpe by agent
    print(df.groupby("agent")["sharpe"].mean())

    # Profit distribution by feature set
    print(df.groupby("features_used")["profit_loss"].describe())


if __name__ == "__main__":
    # generate_overview()
    describe_summary()

