import pandas as pd

def summarize_windows(csv_file, window_col="Window", n_head=3, n_tail=2):
    """
    Summarize daily results by printing first n_head and last n_tail rows per window.
    
    Parameters
    ----------
    csv_file : str
        Path to the CSV file containing daily results.
    window_col : str
        Name of the column identifying the rolling window (default = "window").
    n_head : int
        Number of rows to display from the beginning of each window.
    n_tail : int
        Number of rows to display from the end of each window.
    """
    # Load data
    df = pd.read_csv(csv_file)

    df.columns = [c.lower() for c in df.columns]
    window_col = window_col.lower()

    # Ensure window column exists
    if window_col not in df.columns:
        raise ValueError(f"Column '{window_col}' not found in CSV.")

    # Group by window
    
    for w, group in df.groupby(window_col):
        # print(f"\n=== Window {w} ===")
        # first n_head rows
        print(group.head(n_head).to_string(index=False))
        print("   ...")  # dotted separator
        # last n_tail rows
        print(group.tail(n_tail).to_string(index=False))

