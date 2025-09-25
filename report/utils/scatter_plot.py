import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def plot_scatter_with_regression(df, x_col, y_col, title="Scatter Plot with Regression"):
    """
    Creates a scatter plot with regression line and R² annotation.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset containing the columns.
    x_col : str
        Column name for the x-axis (e.g., "fear_greed_norm").
    y_col : str
        Column name for the y-axis (e.g., "sharpe_ratio").
    title : str
        Plot title.

    Returns
    -------
    None
    """
    
    # X must be 2D for sklearn
    X = df[x_col].values.reshape(-1, 1)
    y = df[y_col].values

    # Fit linear regression
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Calculate R²
    r2 = model.score(X, y)

    # Plot
    plt.figure(figsize=(7, 5))
    plt.scatter(X, y, alpha=0.7, label="Data points")
    plt.plot(X, y_pred, color="red", linewidth=2, label=f"Fit line (R² = {r2:.2f})")

    # Labels and title
    plt.xlabel(x_col.replace("_", " ").title())
    plt.ylabel(y_col.replace("_", " ").title())
    plt.title(title)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()
