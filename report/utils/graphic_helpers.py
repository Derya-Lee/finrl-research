import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

def plot_sharpe_across_phases(df, phase_col="phase", window_col="window", sharpe_col="sharpe_ann"):
    """
    Plot annualized Sharpe ratio across windows for multiple phases.
    
    df: DataFrame containing at least [phase_col, window_col, sharpe_col].
    """
    plt.figure(figsize=(10,6))
    
    for phase, group in df.groupby(phase_col):
        plt.plot(group[window_col], group[sharpe_col], marker="o", label=f"Phase {phase}")
    
    plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
    plt.title("Annualized Sharpe Ratios Across Phases")
    plt.xlabel("Window")
    plt.ylabel("Annualized Sharpe Ratio")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()

#     @staticmethod
def plot_correlation_boxplot(df, title="Correlations across windows"):
    """
    Creates a boxplot of correlation values across windows for each pair.

    Parameters
    ----------
    df : pd.DataFrame
        Must have columns: 'pair', 'value', 'window'
    title : str
        Plot title
    """
    plt.figure(figsize=(8,6))
    sns.boxplot(x="pair", y="value", data=df)

    plt.title(title, fontsize=14)
    plt.ylabel("Correlation value")
    plt.xlabel("Variable pair")
    plt.xticks(rotation=20)
    plt.grid(True, axis="y", linestyle="--", alpha=0.7)

    plt.show()

def correlation_scatter(x, y, xlabel="X", ylabel="Y", title="Correlation Scatterplot"):
    """
    Plots a scatterplot with regression line between two data sets (x, y).

    Parameters:
    -----------
    x : array-like or pandas Series
        Data for X-axis
    y : array-like or pandas Series
        Data for Y-axis
    xlabel : str
        Label for the X-axis
    ylabel : str
        Label for the Y-axis
    title : str
        Title for the chart
    """
    plt.figure(figsize=(7, 5))
    sns.regplot(x=x, y=y, scatter_kws={'color': 'steelblue', 'alpha': 0.7}, line_kws={'color': 'red'})
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=14)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

"""
windows where one phase is clearly stronger (Sharpe difference > 0.5)
windows where they are clustered close together
Phase 2 (risk-aware) and Phase 3 (sentiment-aware)
< 0 	negative
<1.0	suboptimal
<1.99	good
 =<2.99	very good
 =>3.0	excellent
"""
import pandas as pd

def categorize_sharpe(value: float) -> str:
    """Categorize Sharpe ratio based on standard thresholds."""
    if value < 0:
        return "negative"
    elif value < 1.0:
        return "suboptimal"
    elif value < 2.0:
        return "good"
    elif value < 3.0:
        return "very good"
    else:
        return "excellent"

def summarize_sharpe_differences(df, phase_col="phase", window_col="window", sharpe_col="sharpe_ann"):
    """
    Summarize Sharpe ratio differences across phases for each window,
    with categorization of performance quality.
    """
    summary = []
    for w, group in df.groupby(window_col):
        # Ensure phases are integers
        group[phase_col] = group[phase_col].astype(int)

        # Get Sharpe per phase
        diffs = group.set_index(phase_col)[sharpe_col]
        max_phase = int(diffs.idxmax())
        min_phase = int(diffs.idxmin())
        max_val = diffs.max()
        min_val = diffs.min()
        diff = max_val - min_val

        # Categorize difference
        if diff > 0.5:
            category = "large difference"
        elif diff < 0.2:
            category = "similar"
        else:
            category = "moderate difference"

        summary.append({
            "window": w,
            "best_phase": max_phase,
            "worst_phase": min_phase,
            "best_sharpe": max_val,
            "best_category": categorize_sharpe(max_val),
            "worst_sharpe": min_val,
            "worst_category": categorize_sharpe(min_val),
            "diff": diff,
            "comparison": category
        })

    return pd.DataFrame(summary)

# def summarize_sharpe_differences(df, phase_col="phase", window_col="window", sharpe_col="sharpe_ann"):
#     summary = []
#     for w, group in df.groupby(window_col):
#         diffs = group.set_index(phase_col)[sharpe_col]
#         max_phase = diffs.idxmax()
#         min_phase = diffs.idxmin()
#         max_val = diffs.max()
#         min_val = diffs.min()
#         diff = max_val - min_val
        
#         if diff > 0.5:  # large gap
#             summary.append((w, max_phase, min_phase, diff, "large difference"))
#         elif diff < 0.2:  # convergence
#             summary.append((w, None, None, diff, "similar"))
#         else:
#             summary.append((w, max_phase, min_phase, diff, "moderate difference"))
    
#     return pd.DataFrame(summary, columns=["window", "best_phase", "worst_phase", "diff", "category"])


# Cumulative Return Trajectories
# k-means