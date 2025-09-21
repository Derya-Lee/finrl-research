import pandas as pd

import os

# from utils.graphic_helpers import PlotTools

#---------
# 31 Aug 2025
# NOTE : results - drive / Descriptive (Correlations) Analysis
#---------

current_dir = os.path.dirname(__file__)
#input data from results:
data_path = os.path.join(current_dir, "data")

results_path = os.path.join(current_dir, "results")
voltur_stats_file = os.path.join(results_path, "voltur_wind_stats.csv")
voltur_corrs_file = os.path.join(results_path, "voltur_correlations.csv")

sen_corr_file_a =  os.path.join(results_path, "normalized_sen_correlations.csv") 
sen_corr_file_b =  os.path.join(results_path, "mapped_sen_correlations.csv") 

sen_stats_file_a =  os.path.join(results_path, "normalized_sen_stats.csv") 
sen_stats_file_b =  os.path.join(results_path, "mapped_sen_stats.csv") 

   

def generate_descriptive_stats():
    phase2_results = os.path.join(data_path, "ft_account_values.csv")
    phase3a_results = os.path.join(data_path, "sen_account_values_norm.csv")
    phase3b_results = os.path.join(data_path, "sen_account_values_mapped.csv")

    # --- Descriptive statistics for Phase 2 --- # 
    # PHASE 2 vol-tur correlations
    phase2_df = pd.read_csv(phase2_results, parse_dates=["date"])
    phase2_corrs = voltur_correlations(phase2_df)
    phase2_corrs.to_csv(voltur_corrs_file,  index=False)
    
    # #  PHASE 2  vol-tur statistics
    voltur_stats = voltur_summary_stats(phase2_df)
    df_results_summary = pd.DataFrame(voltur_stats)
    df_results_summary.to_csv(voltur_stats_file, index=False)

     # --- Descriptive statistics for Phase 3 a & b (using normalized and mapped values respectivelly)--- # 

    norm_feargreed_df = pd.read_csv(phase3a_results, parse_dates=["date"])
    norm_feargreed_corr_df = feargreed_correlations_pearson(norm_feargreed_df)
    norm_feargreed_corr_df.to_csv(sen_corr_file_a, index=False)

 
    mapped_feargreed_df = pd.read_csv(phase3b_results, parse_dates=["date"], thousands=",")
    
    # DEBUG fixed: account_value dissepears due to number formatting 
    # NOTE: either don't use "parse_dates=["date"]" or add thousands=","
    # print(mapped_feargreed_df["account_value"].head(20).to_list())
    # print(mapped_feargreed_df.dtypes)
    # print(mapped_feargreed_df["account_value"].unique()[:10])  # sample unique values
    
    mapped_feargreed_corr_df = feargreed_correlations_spearman(mapped_feargreed_df)
    mapped_feargreed_corr_df.to_csv(sen_corr_file_b, index=False)

    feargreed_stats_norm =  (
        norm_feargreed_df.groupby("window")[["account_value", "daily_return", "fear_greed", "fear_greed_norm"]]
        .describe()
    )

    feargreed_stats_norm.to_csv(sen_stats_file_a, index=False)

    feargreed_stats_mapped =  (
        mapped_feargreed_df.groupby("window")[["account_value", "daily_return", "fear_greed_mapped"]]
        .describe()
    )
    feargreed_stats_mapped.to_csv(sen_stats_file_b, index=False)

#---------
#
#---------
def voltur_summary_stats(df):
    # Compute summary stats for each window
    window_stats = (
        df.groupby("window")[["account_value", "daily_return", "volatility", "turbulence"]]
        .describe()
    )

    print(window_stats)
    return window_stats

#---------
# Drop self-correlations and duplicates
#---------
def clean_duplicates(corr_flat):
        # Create a consistent pair label (alphabetical order of names)
        corr_flat["pair"] = corr_flat.apply(
            lambda row: " ~ ".join(sorted([row["index"], row["variable"]])), axis=1
        )

        # Drop self-correlations and duplicates
        corr_flat = corr_flat[corr_flat["index"] != corr_flat["variable"]]
        corr_flat = corr_flat.drop_duplicates(subset=["pair", "window"])

        return corr_flat
#---------
# Create correlations (between variables) for all windows for analysis or plotting
# Return averages for reporting
#---------
def voltur_correlations(df):

    correlations = {}
    all_corrs = []

    for w, g in df.groupby("window"):
        corr = g[["daily_return", "volatility", "turbulence"]].corr()
        correlations[w] = corr
        # all windows for analysis or plotting.
        corr_flat = corr.reset_index().melt(id_vars="index")
        corr_flat["window"] = w

        # Create a consistent pair label (alphabetical order of names)
        corr_flat["pair"] = corr_flat.apply(
            lambda row: " ~ ".join(sorted([row["index"], row["variable"]])), axis=1
        )

        # Drop self-correlations and duplicates
        corr_flat = corr_flat[corr_flat["index"] != corr_flat["variable"]]
        corr_flat = corr_flat.drop_duplicates(subset=["pair", "window"])

        all_corrs.append(corr_flat[["pair", "value", "window"]])


    all_corrs_df = pd.concat(all_corrs)
 
    return all_corrs_df

#---------
# use normalized version ((x-50)/50) for correlation and regression analysis, since it puts the data on a symmetric scale (centered around 0).
#---------
def feargreed_correlations_pearson(df):

    correlations = {}
    all_corrs = []
    # note: not including fear_greed_mapped as it is categorical and not meaningful for correlation
    for w, g in df.groupby("window"):
        pearson_corr = g[["daily_return", "fear_greed", "fear_greed_norm"]].corr(method="pearson")
        correlations[w] = pearson_corr

                # all windows for analysis or plotting.
        corr_flat = pearson_corr.reset_index().melt(id_vars="index")
        corr_flat["window"] = w

        corr_flat = clean_duplicates(corr_flat)
        corr_flat = corr_flat[(corr_flat["index"] == "daily_return") | (corr_flat["variable"] == "daily_return")]

        all_corrs.append(corr_flat[["pair", "value", "window"]])

    all_corrs_df = pd.concat(all_corrs)
    return all_corrs_df

#---------
# uses mapped version
#---------
def feargreed_correlations_spearman(df):

    correlations = {}
    all_corrs = []
    for w, g in df.groupby("window"):
        spearman_corr = g[["daily_return", "fear_greed_mapped"]].corr(method="spearman")
        correlations[w] = spearman_corr

                # all windows for analysis or plotting.
        corr_flat = spearman_corr.reset_index().melt(id_vars="index")
        corr_flat["window"] = w

        corr_flat = clean_duplicates(corr_flat)
        corr_flat = corr_flat[(corr_flat["index"] == "daily_return") | (corr_flat["variable"] == "daily_return")]

        all_corrs.append(corr_flat[["pair", "value", "window"]])

    all_corrs_df = pd.concat(all_corrs)
    return all_corrs_df




if __name__ == "__main__":
    generate_descriptive_stats()
