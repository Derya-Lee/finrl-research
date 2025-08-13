import pandas as pd
from dateutil.relativedelta import relativedelta

def test_rolling_windows_structure():
    from finrl.utils.rolling_windows import get_rolling_windows  
    from finrl.config import (TRAIN_START_DATE, TRAIN_END_DATE, TEST_START_DATE, TEST_END_DATE, TRADE_START_DATE, TRADE_END_DATE)


    TRAIN_WINDOW_MONTHS = 6
    VALIDATION_WINDOW_MONTHS = 2
    TRADE_WINDOW_MONTHS = 2

    windows = get_rolling_windows(
        train_months=TRAIN_WINDOW_MONTHS,
        val_months=VALIDATION_WINDOW_MONTHS,
        trade_months=TRADE_WINDOW_MONTHS,
        start_date_str=TRAIN_START_DATE,
        end_date_str=TRADE_END_DATE
    )

    # Collect info for table
    table_rows = []
    for i, (train_start, train_end, val_start, val_end, trade_start, trade_end) in enumerate(windows):

        table_rows.append({
            "Window": i + 1,
            "Train Start": train_start.date(),
            "Train End": train_end.date(),
            "Val Start": val_start.date(),
            "Val End": val_end.date(),
            "Trade Start": trade_start.date(),
            "Trade End": trade_end.date()
        })

    # df_windows = pd.DataFrame(table_rows)
    # print("\n Rolling Windows Overview:")
    # print(df_windows.to_string(index=False))
    # return df_windows

def test_rolling_windows_less():
    from finrl.utils.rolling_windows import get_rolling_windows  
    from finrl.config import (TRAIN_START_DATE, TRAIN_END_DATE, TEST_START_DATE, TEST_END_DATE, TRADE_START_DATE, TRADE_END_DATE)

    START_DATE = "2021-01-01"  
    start_dt = pd.Timestamp("2021-01-01")
    END_DATE = start_dt + pd.DateOffset(days=360)

    windows = get_rolling_windows(
        train_months=1,
        val_months=1,
        trade_months=1,
        start_date_str=START_DATE,
        end_date_str=END_DATE
    )

    # Collect info for table
    table_rows = []
    for i, (train_start, train_end, val_start, val_end, trade_start, trade_end) in enumerate(windows):

        table_rows.append({
            "Window": i + 1,
            "Train Start": train_start.date(),
            "Train End": train_end.date(),
            "Val Start": val_start.date(),
            "Val End": val_end.date(),
            "Trade Start": trade_start.date(),
            "Trade End": trade_end.date()
        })