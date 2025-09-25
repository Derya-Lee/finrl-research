import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_rel

def compare_experiments(expA, expB, metric_name, experiment_name, windows=None, save_plots=False):
    """
    Compare performance of Experiment 3a vs 3b for a given metric.
    
    Parameters:
    -----------
    expA : array-like
        Values for Experiment 3a.
    expB : array-like
        Values for Experiment 3b.
    metric_name : str
        Name of the metric (e.g., 'annualized_sharpe').
    windows : array-like, optional
        Window numbers for x-axis in lineplot. If None, use index.
    save_plots : bool, optional
        If True, saves plots as PNG instead of showing them.
    
    Returns:
    --------
    summary : dict
        Summary statistics and t-test results.
    """
    
    df = pd.DataFrame({
        "exp_a": expA,
        "exp_b": expB
    })
    df["diff"] = df["exp_a"] - df["exp_b"]
    if windows is not None:
        df["window"] = windows
    else:
        df["window"] = range(1, len(df) + 1)
    
    # --- Summary statistics ---
    summary = {
        "metric": metric_name,
        "mean_diff": df["diff"].mean(),
        "median_diff": df["diff"].median(),
        "positive_windows": int((df["diff"] > 0).sum()),
        "negative_windows": int((df["diff"] < 0).sum())
    }
    
    # --- Paired t-test ---
    stat, pval = ttest_rel(df["exp_a"], df["exp_b"])
    summary["t_stat"] = stat
    summary["p_value"] = pval
    
    # --- Lineplot ---
    plt.figure(figsize=(10,5))
    plt.plot(df["window"], df["exp_a"], marker="o", label="Experiment a")
    plt.plot(df["window"], df["exp_b"], marker="s", label="Experiment b")
    plt.title(f"{metric_name}: {experiment_name}")
    plt.xlabel("Window")
    plt.ylabel(metric_name)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)
    
    if save_plots:
        plt.savefig(f"{metric_name}_lineplot.png", dpi=300, bbox_inches="tight")
        plt.close()
    else:
        plt.show()
    
    # --- Boxplot ---
    melted = df.melt(id_vars="window", value_vars=["exp_a", "exp_b"],
                     var_name="Experiment", value_name=metric_name)
    plt.figure(figsize=(6,5))
    sns.boxplot(x="Experiment", y=metric_name, data=melted)
    plt.title(f"Distribution of {metric_name} across windows")
    
    if save_plots:
        plt.savefig(f"{metric_name}_boxplot.png", dpi=300, bbox_inches="tight")
        plt.close()
    else:
        plt.show()
    
    return summary


def compare_all_metrics(metrics_dict, windows=None, experiment_name=None, save_csv=True, save_plots=False, csv_name="experiment_comparison_summary.csv"):
    """
    Run comparisons for multiple metrics and optionally save results to CSV.
    
    Parameters:
    -----------
    metrics_dict : dict
        Dictionary where keys = metric names, values = (expA_array, expB_array).
    windows : array-like, optional
        Window numbers.
    save_csv : bool
        Save summary table to CSV.
    save_plots : bool
        Save plots instead of showing them.
    csv_name : str
        Output CSV filename.
    
    Returns:
    --------
    summary_df : pd.DataFrame
        DataFrame with summary results for all metrics.
    """
    results = []
    for metric_name, (expA, expB) in metrics_dict.items():
        summary = compare_experiments(expA, expB, metric_name, experiment_name, windows=windows, save_plots=save_plots)
        
        df = pd.DataFrame({
        "exp_a": expA,
        "exp_b": expB
        })
        df["diff"] = df["exp_a"] - df["exp_b"]
        if windows is not None:
            df["window"] = windows
        else:
            df["window"] = range(1, len(df) + 1)
        
        # --- Summary statistics ---
        summary = {
            "metric": metric_name,
            "mean_diff": df["diff"].mean(),
            "median_diff": df["diff"].median(),
            "positive_windows": int((df["diff"] > 0).sum()),
            "negative_windows": int((df["diff"] < 0).sum())
        }
        
        # --- Paired t-test ---
        stat, pval = ttest_rel(df["exp_a"], df["exp_b"])
        summary["t_stat"] = stat
        summary["p_value"] = pval
    
        results.append(summary)
    summary_df = pd.DataFrame(results)
    
    if save_csv:
        summary_df.to_csv(csv_name, index=False)
    
    return summary_df


def plot_window_comparison(df, win_a=14, win_b=5,
                           date_col="date", 
                           exp2_col="Exp_2_Account_Value", 
                           exp3_col="Exp_3_Account_Value", 
                           window_col="window"):
    """
    Plot Exp.2 vs Exp.3 % differences for two windows on the same chart.
    Dates are shown as day counts (0, 1, 2, …) to keep the x-axis clean.
    """

    # Filter for each window
    df_a = df[df[window_col] == win_a].copy()
    df_b = df[df[window_col] == win_b].copy()

    # Reset index to make day counts
    df_a = df_a.reset_index(drop=True)
    df_b = df_b.reset_index(drop=True)

    # Calculate percentage difference (Exp.3 - Exp.2) / Exp.2
    df_a["perc_diff"] = (df_a[exp3_col] - df_a[exp2_col]) / df_a[exp2_col] * 100
    df_b["perc_diff"] = (df_b[exp3_col] - df_b[exp2_col]) / df_b[exp2_col] * 100

    plt.figure(figsize=(10, 6))

    # Plot both windows
    plt.plot(df_a.index, df_a["perc_diff"], label=f"Window {win_a}", marker="o")
    plt.plot(df_b.index, df_b["perc_diff"], label=f"Window {win_b}", marker="o")

    plt.axhline(0, color="gray", linestyle="--", linewidth=1)

    plt.xlabel("Day (relative to window start)")
    plt.ylabel("Exp.3 vs Exp.2 Difference (%)")
    plt.title(f"Comparison of Exp.3 vs Exp.2 Performance\nWindows {win_a} and {win_b}")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()
