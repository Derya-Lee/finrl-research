import matplotlib.pyplot as plt
import seaborn as sns


def plot_dashboard(account_values_df, metrics_df):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # 1. Account value by window
    sns.lineplot(data=account_values_df, x="date", y="account_value", hue="window", ax=axes[0, 0])
    axes[0, 0].set_title("Account Value Over Time")

    # 2. Rewards over time
    sns.lineplot(data=account_values_df, x="date", y="reward", hue="window", ax=axes[0, 1])
    axes[0, 1].set_title("Daily Rewards Over Time")

    # 3. Trade counts
    sns.barplot(data=account_values_df, x="window", y="trade_count", ax=axes[1, 0], ci=None)
    axes[1, 0].set_title("Number of Trades per Window")

    # 4. Volatility by window
    sns.barplot(data=metrics_df, x="window", y="volatility (std)", ax=axes[1, 1], ci=None)
    axes[1, 1].set_title("Volatility by Window")

    plt.tight_layout()
    plt.show()    

# # Account Value over Time per Window - A line plot with each window as a separate color to show equity curve stability and volatility.
# def plot_account_values(account_values):
#     plt.figure(figsize=(12, 6))
#     sns.lineplot(data=account_values, x="date", y="account_value", hue="window", palette="tab10")
#     plt.title("Account Value Over Time by Window")
#     plt.ylabel("Account Value ($)")
#     plt.xlabel("Date")
#     plt.legend(title="Window")
#     plt.grid(True)
#     plt.show()

# # Trade Counts vs. Reward Scatter plot to see if more trades = higher/lower rewards.
# def plot_counts_rewards(account_values):
#     plt.figure(figsize=(8, 6))
#     sns.scatterplot(data=account_values, x="trade_count", y="reward", hue="window", palette="tab10", alpha=0.7)
#     plt.title("Trade Count vs Daily Reward")
#     plt.xlabel("Number of Trades")
#     plt.ylabel("Daily Reward")
#     plt.grid(True)
#     plt.show()

# # Volatility vs. Total Return per Window - a “risk vs. reward” plot.
# def plot_volatility_return(metrics):
#     plt.figure(figsize=(8, 6))
#     sns.scatterplot(data=metrics, x="volatility (std)", y="total_return", hue="agent", s=100)
#     for i, row in metrics.iterrows():
#         plt.text(row["volatility (std)"], row["total_return"], f"W{row['window']}", fontsize=9)
#     plt.title("Return vs Volatility per Window")
#     plt.xlabel("Volatility (std)")
#     plt.ylabel("Total Return")
#     plt.grid(True)
#     plt.show()

# #  Sharpe Ratio per Window - Bar chart to compare models/windows.
# def plot_sharp_window(metrics):
#     plt.figure(figsize=(10, 6))
#     sns.barplot(data=metrics, x="window", y="sharpe_ratio", hue="agent", palette="Set2")
#     plt.title("Sharpe Ratio per Window")
#     plt.ylabel("Sharpe Ratio")
#     plt.xlabel("Window")
#     plt.grid(True, axis="y")
#     plt.show()

