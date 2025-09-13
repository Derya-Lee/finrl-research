import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from dateutil.relativedelta import relativedelta
# from finrl.config import TRAIN_LEN, VAL_LEN, TRADE_LEN
from finrl.meta.preprocessor.preprocessors import FeatureEngineer, data_split

from pathlib import Path





def test_rolling_windows():
    from finrl.utils.rolling_windows import get_rolling_windows  
    from finrl.config import (TRAIN_START_DATE, TRADE_END_DATE)
  
    data_path = "../data/binance_less_raw.csv"

    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, "data")
    dt_processed_path = os.path.join(data_path, "processed_bnc_data.csv")


    START_DATE = pd.Timestamp(TRAIN_START_DATE)
    END_DATE = pd.Timestamp(TRADE_END_DATE)

# def get_rolling_windows(train_months=1, val_months=1, trade_months=1, 
#                         start_date_str=TRAIN_START_DATE, 
#                         end_date_str=TRADE_END_DATE,
#                         lookback_days=MAX_LOOKBACK):
    
    # windows = get_rolling_windows(
    #     train_months=TRAIN_LEN,
    #     val_months=VAL_LEN,
    #     trade_months=TRADE_LEN,
    #     start_date_str=START_DATE,
    #     end_date_str=END_DATE
    # )

    windows = get_rolling_windows(
        train_months=12,
        val_months=1,
        trade_months=1,
        start_date_str=START_DATE,
        end_date_str=END_DATE,
        lookback_days=60
    )

    # Collect info for table
    table_rows = []



 
    dt_processed_path = os.path.join(data_path, "processed_bnc_data.csv")
    df_processed = pd.read_csv(dt_processed_path, parse_dates=["date"])
    
    # trainData = []
    # valData = []
    # tradeData = []
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

        # train_data = data_split(df_processed, train_start.date(), train_end.date())
        # val_data = data_split(df_processed, val_start.date(), val_end.date())
        # trade_data = data_split(df_processed, trade_start.date(), trade_end.date())

        # trainData.append(train_data)
        # valData.append(val_data)
        # tradeData.append(trade_data)
    print(table_rows)
# --------Print dates in table view --------------------
    df_windows = pd.DataFrame(table_rows)
    print("\n Rolling Windows Overview:")
    print(df_windows.to_string(index=False))
# ------------------------------------------------------

if __name__ == "__main__":
    test_rolling_windows()

#  Rolling Windows Overview:
#  Window, Train Start, Train End,  Val Start,    Val End, Trade Start,  Trade End
#       1,  2020-05-04, 2021-05-03, 2021-05-04, 2021-08-02,  2021-08-03, 2021-11-01
#       2,  2020-07-04, 2021-07-03, 2021-07-04, 2021-10-02,  2021-10-03, 2022-01-01
#       3,  2020-09-04, 2021-09-03, 2021-09-04, 2021-12-02,  2021-12-03, 2022-03-03
#       4,  2020-11-04, 2021-11-03, 2021-11-04, 2022-02-01,  2022-02-02, 2022-04-30
#       5,  2021-01-04, 2022-01-03, 2022-01-04, 2022-04-04,  2022-04-05, 2022-07-03
#       6,  2021-03-04, 2022-03-03, 2022-03-04, 2022-06-02,  2022-06-03, 2022-08-31
#       7,  2021-05-04, 2022-05-03, 2022-05-04, 2022-08-02,  2022-08-03, 2022-11-01
#       8,  2021-07-04, 2022-07-03, 2022-07-04, 2022-10-02,  2022-10-03, 2023-01-01
#       9,  2021-09-04, 2022-09-03, 2022-09-04, 2022-12-02,  2022-12-03, 2023-03-03
#      10,  2021-11-04, 2022-11-03, 2022-11-04, 2023-02-01,  2023-02-02, 2023-04-30
#      11,  2022-01-04, 2023-01-03, 2023-01-04, 2023-04-04,  2023-04-05, 2023-07-03
#      12,  2022-03-04, 2023-03-03, 2023-03-04, 2023-06-02,  2023-06-03, 2023-08-31
#      13,  2022-05-04, 2023-05-03, 2023-05-04, 2023-08-02,  2023-08-03, 2023-11-01
#      14,  2022-07-04, 2023-07-03, 2023-07-04, 2023-10-02,  2023-10-03, 2024-01-01
#      15,  2022-09-04, 2023-09-03, 2023-09-04, 2023-12-02,  2023-12-03, 2024-03-02
#      16,  2022-11-04, 2023-11-03, 2023-11-04, 2024-02-01,  2024-02-02, 2024-04-30
#      17,  2023-01-04, 2024-01-03, 2024-01-04, 2024-04-03,  2024-04-04, 2024-07-02
#      18,  2023-03-04, 2024-03-03, 2024-03-04, 2024-06-02,  2024-06-03, 2024-08-31
#      19,  2023-05-04, 2024-05-03, 2024-05-04, 2024-08-02,  2024-08-03, 2024-11-01
#      20,  2023-07-04, 2024-07-03, 2024-07-04, 2024-10-02,  2024-10-03, 2025-01-01
#      21,  2023-09-04, 2024-09-03, 2024-09-04, 2024-12-02,  2024-12-03, 2025-03-03
#      22,  2023-11-04, 2024-11-03, 2024-11-04, 2025-02-01,  2025-02-02, 2025-04-30







