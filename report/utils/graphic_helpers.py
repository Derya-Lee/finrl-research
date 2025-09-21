import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

from scipy.stats import pearsonr, spearmanr

def plot_sentiment_vs_performance(sentiment, performance, metric_name="Max Drawdown", sentiment_name="Fear & Greed", windows=None):
    """
    Scatterplot of sentiment vs performance metric across windows, with regression line and correlation stats.

    Parameters
    ----------
    sentiment : list or array
        Window-level sentiment values (mean, median, IQR, etc.)
    performance : list or array
        Window-level performance metric (e.g., max_drawdown, sharpe)
    metric_name : str
        Label for the performance metric (used in title and y-axis label)
    sentiment_name : str
        Label for the sentiment measure (used in title and x-axis label)
    windows : list or array, optional
        Window numbers for labeling/coloring. If None, simple index is used.
    """
    if windows is None:
        windows = np.arange(1, len(sentiment) + 1)

    # Compute correlations
    pearson_corr, pearson_p = pearsonr(sentiment, performance)
    spearman_corr, spearman_p = spearmanr(sentiment, performance)

    plt.figure(figsize=(8, 6))
    scatter = sns.scatterplot(x=sentiment, y=performance, hue=windows, palette="viridis", s=80)

    # regression line (linear fit)
    sns.regplot(x=sentiment, y=performance, scatter=False, ci=None, color="red", line_kws={"linewidth": 2})

    plt.xlabel(f"{sentiment_name} (per window)")
    plt.ylabel(metric_name)
    plt.title(f"{sentiment_name} vs {metric_name}")

    # correlation annotation
    plt.text(0.05, 0.95, 
             f"Pearson r = {pearson_corr:.2f} (p={pearson_p:.3f})\nSpearman ρ = {spearman_corr:.2f} (p={spearman_p:.3f})",
             transform=plt.gca().transAxes,
             fontsize=10,
             verticalalignment="top",
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.6))

    plt.legend(title="Window", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()



def plot_sentiment_vs_performance_diff(sentiment, performance, metric_name="Max Drawdown", sentiment_name="Fear & Greed", windows=None):
    """
    Scatterplot of sentiment vs performance metric across windows, with regression line and correlation stats.

    Parameters
    ----------
    sentiment : list or array
        Window-level sentiment values (mean, median, IQR, etc.)
    performance : list or array
        Window-level performance metric (e.g., max_drawdown, sharpe)
    metric_name : str
        Label for the performance metric (used in title and y-axis label)
    sentiment_name : str
        Label for the sentiment measure (used in title and x-axis label)
    windows : list or array, optional
        Window numbers for labeling/coloring. If None, simple index is used.
    """
    if windows is None:
        windows = np.arange(1, len(sentiment) + 1)

    # Compute correlations
    pearson_corr, pearson_p = pearsonr(sentiment, performance)
    spearman_corr, spearman_p = spearmanr(sentiment, performance)

    plt.figure(figsize=(8, 6))
    scatter = sns.scatterplot(x=sentiment, y=performance, hue=windows, palette="viridis", s=80)

    # regression line (linear fit)
    sns.regplot(x=sentiment, y=performance, scatter=False, ci=None, color="red", line_kws={"linewidth": 2})

    plt.xlabel(f"{sentiment_name} (per window)")
    plt.ylabel(metric_name)
    plt.title(f"{sentiment_name} vs {metric_name}")

    # correlation annotation
    plt.text(0.05, 0.95, 
             f"Pearson r = {pearson_corr:.2f} (p={pearson_p:.3f})\nSpearman ρ = {spearman_corr:.2f} (p={spearman_p:.3f})",
             transform=plt.gca().transAxes,
             fontsize=10,
             verticalalignment="top",
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.6))

    plt.legend(title="Window", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def categorize_fear_greed(norm_values, scale="0-1"):
    """
    Categorize normalized Fear & Greed values into Alternative.me categories.
    
    Parameters
    ----------
    norm_values : pd.Series or array
        Fear & Greed values normalized either to [0,1] or [-1,1].
    scale : str
        "0-1" if normalized to [0,1], "neg1-1" if normalized to [-1,1].
    """
    categories = []
    for v in norm_values:
        if scale == "0-1":
            if v <= 0.24:
                categories.append("Extreme Fear")
            elif v <= 0.49:
                categories.append("Fear")
            elif v <= 0.74:
                categories.append("Greed")
            else:
                categories.append("Extreme Greed")
        elif scale == "neg1-1":
            if v <= -0.52:
                categories.append("Extreme Fear")
            elif v <= -0.02:
                categories.append("Fear")
            elif v <= 0.48:
                categories.append("Greed")
            else:
                categories.append("Extreme Greed")
        else:
            raise ValueError("scale must be '0-1' or 'neg1-1'")
    return categories


def plot_drawdowns_by_sentiment(fg_values, drawdowns, scale="0-1"):
    """
    Plot distribution of drawdowns across Fear & Greed sentiment categories.

    Parameters
    ----------
    fg_values : array-like
        Normalized Fear & Greed values.
    drawdowns : array-like
        Max drawdown (or daily returns) aligned with fg_values.
    scale : str
        Normalization type ("0-1" or "neg1-1").
    """
    df = pd.DataFrame({
        "FearGreed": fg_values,
        "Drawdown": drawdowns
    })
    df["Category"] = categorize_fear_greed(df["FearGreed"], scale=scale)

    plt.figure(figsize=(8,6))
    sns.boxplot(x="Category", y="Drawdown", data=df, order=["Extreme Fear","Fear","Greed","Extreme Greed"])
    sns.stripplot(x="Category", y="Drawdown", data=df, order=["Extreme Fear","Fear","Greed","Extreme Greed"],
                  color="black", alpha=0.5, jitter=True)

    plt.title("Drawdowns by Fear & Greed Category")
    plt.ylabel("Max Drawdown (or Daily Return)")
    plt.xlabel("Fear & Greed Category")
    plt.show()

    return df
