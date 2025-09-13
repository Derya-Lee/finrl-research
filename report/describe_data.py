import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
current_dir = os.path.dirname(__file__)
results_path = os.path.join(current_dir, "results")
os.makedirs(results_path, exist_ok=True)
results_file = os.path.join(results_path, "combined_summary.csv")

def describe_summary(results_file):
    df = pd.read_csv(results_file)

    # --- 1. Average Sharpe by feature set ---
    sharpe_by_feature = df.groupby("features_used")["sharpe"].mean().reset_index()
    print("\nAverage Sharpe by Feature Set:")
    print(sharpe_by_feature)

    # --- 2. Average Sharpe by agent ---
    sharpe_by_agent = df.groupby("agent")["sharpe"].mean().reset_index()
    print("\nAverage Sharpe by Agent:")
    print(sharpe_by_agent)

    # --- 3. Profit distribution by feature set ---
    profit_stats = df.groupby("features_used")["profit_loss"].describe()
    print("\nProfit Distribution by Feature Set:")
    print(profit_stats)

    # --- 📊 Visualization section ---

    # Sharpe ratio by features
    plt.figure(figsize=(6,4))
    sns.barplot(data=sharpe_by_feature, x="features_used", y="sharpe", palette="viridis")
    plt.title("Average Sharpe Ratio by Feature Set")
    plt.ylabel("Sharpe Ratio")
    plt.xlabel("Features Used")
    plt.tight_layout()
    plt.savefig("results/sharpe_by_feature.png")
    plt.show()

    # Sharpe ratio by agent
    plt.figure(figsize=(6,4))
    sns.barplot(data=sharpe_by_agent, x="agent", y="sharpe", palette="magma")
    plt.title("Average Sharpe Ratio by Agent")
    plt.ylabel("Sharpe Ratio")
    plt.xlabel("Agent")
    plt.tight_layout()
    plt.savefig("results/sharpe_by_agent.png")
    plt.show()

    # Profit distribution (boxplot)
    plt.figure(figsize=(6,4))
    sns.boxplot(data=df, x="features_used", y="profit_loss", palette="Set2")
    plt.title("Profit/Loss Distribution by Feature Set")
    plt.ylabel("Profit / Loss")
    plt.xlabel("Features Used")
    plt.tight_layout()
    plt.savefig("results/profit_distribution.png")
    plt.show()

    return sharpe_by_feature, sharpe_by_agent, profit_stats


if __name__ == "__main__":
    describe_summary("results/combined_summary.csv")

