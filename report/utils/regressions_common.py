# regression_helpers.py
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd

def run_simple_regression(df, y_col, x_col):
    """
    Runs a simple OLS regression (y ~ x).

    Parameters:
    -----------
    df : pandas.DataFrame
        Data containing both y and x.
    y_col : str
        Dependent variable column name.
    x_col : str
        Independent variable column name.

    Returns:
    --------
    results : statsmodels RegressionResults
    """
    formula = f"Q('{y_col}') ~ Q('{x_col}')"
    model = smf.ols(formula=formula, data=df).fit(cov_type="HC3")
  
    return model


def run_multiple_regression(df, y_col, x_cols):
    """
    Runs a multiple OLS regression (y ~ x1 + x2 + ...).

    Parameters:
    -----------
    df : pandas.DataFrame
        Data containing both y and x.
    y_col : str
        Dependent variable column name.
    x_cols : list of str
        List of independent variable column names.

    Returns:
    --------
    results : statsmodels RegressionResults
    """
    predictors = " + ".join([f"Q('{col}')" for col in x_cols])
    formula = f"Q('{y_col}') ~ {predictors}"
    model = smf.ols(formula=formula, data=df).fit(cov_type="HC3")
    return model


def summarize_results(model):
    """
    Returns a tidy summary with coefficients, p-values, and R-squared.
    """
    summary_df = pd.DataFrame({
        "coef": model.params,
        "pval": model.pvalues,
        "t": model.tvalues
    })
    return {
        "summary_table": summary_df,
        "r2": model.rsquared,
        "adj_r2": model.rsquared_adj
    }

def regression_summary_table(model, model_name="Model"):
    """
    Return a compact summary table with coefficients, std err, t, p-values,
    plus R² and Adj R².
    """
    params = model.params
    conf = model.conf_int()
    table = pd.DataFrame({
        "coef": model.params.round(4),
        "std err": model.bse.round(4),
        "t": model.tvalues.round(2),
        "p>|t|": model.pvalues.round(4),
        "[0.025": conf[0].round(4),
        "0.975]": conf[1].round(4),
    })
    table.index.name = "Variable"
    table = table.reset_index()
    
    # Add model fit stats at the bottom
    fit_stats = pd.DataFrame({
        "Variable": ["R-squared", "Adj. R-squared"],
        "coef": [model.rsquared.round(3), model.rsquared_adj.round(3)]
    })
    fit_stats["std err"] = ""
    fit_stats["t"] = ""
    fit_stats["p>|t|"] = ""
    fit_stats["[0.025"] = ""
    fit_stats["0.975]"] = ""
    
    final_table = pd.concat([table, fit_stats], ignore_index=True)
    final_table.insert(0, "Model", model_name)
    
    return final_table