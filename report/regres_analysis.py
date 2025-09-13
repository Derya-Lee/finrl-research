import pandas as pd
import statsmodels.api as sm
import os

current_dir = os.path.dirname(__file__)
#input data from results:
data_path = os.path.join(current_dir, "data")

# input file
perf_metrics = os.path.join(data_path, "performance_metrics.csv")
# phase1_daily = os.path.join(data_path, "account_values.csv")



# # # output to:
# # results_path = os.path.join(current_dir, "results")
# # voltur_file = os.path.join(results_path, "s.csv")
# # sen_ =  os.path.join(results_path, ".csv") 
# # sen_ =  os.path.join(results_path, ".csv") 


# def bivariate_regression(df):
#     X = df["volatility"]
#     y = df["daily_return"]

#     X = sm.add_constant(X)  # add intercept
#     model = sm.OLS(y, X).fit()
#     print(model.summary())

def regression_analysis():

    df = pd.read_csv(perf_metrics)

    # Filter for Phase 1 (Control Group)
    df_phase1 = df[df["Phase"] == '1']
    df_phase2 = df[df["Phase"] == '2']
    df_phase3a = df[df["Phase"] == '3a']
    df_phase3b = df[df["Phase"] == '3b']


    # # Debug :
    # print(df_phase1.head())
    # print(df_phase2.head())
    # print(df_phase3a.head())
    # print(df_phase3b.head())

    # Regression: daily_return (totals per window) explained by window Sharpe
    import statsmodels.formula.api as smf 

    # Annualized return explained by Sharpe
    model_phase1 = smf.ols("Q('Total Return (ann.)') ~ Q('Annualized Sharpe')", data=df_phase1).fit()
    print(model.summary())

    # Annualized return explained by Sharpe
    model = smf.ols("Q('Total Return (ann.)') ~ Q('Annualized Sharpe')", data=df_phase2).fit()
    print(model.summary())

    #  # Annualized return explained by Sharpe
    model = smf.ols("Q('Total Return (ann.)') ~ Q('Annualized Sharpe')", data=df_phase3a).fit()
    print(model.summary())

     # Annualized return explained by Sharpe
    model = smf.ols("Q('Total Return (ann.)') ~ Q('Annualized Sharpe')", data=df_phase3b).fit()
    print(model.summary())

if __name__ == "__main__":
    regression_analysis()
