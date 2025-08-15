import pandas as pd
from dateutil.relativedelta import relativedelta
from finrl.config import TRAIN_LEN, VAL_LEN, TRADE_LEN
from finrl.meta.preprocessor.preprocessors import FeatureEngineer, data_split

import os
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
    
    windows = get_rolling_windows(
        train_months=TRAIN_LEN,
        val_months=VAL_LEN,
        trade_months=TRADE_LEN,
        start_date_str=START_DATE,
        end_date_str=END_DATE
    )

    # Collect info for table
    table_rows = []



    df_windows = pd.DataFrame(table_rows)
    # print("\n Rolling Windows Overview:")
    # print(df_windows.to_string(index=False))
    dt_processed_path = os.path.join(data_path, "processed_bnc_data.csv")
    df_processed = pd.read_csv(dt_processed_path, parse_dates=["date"])
    
    trainData = []
    valData = []
    tradeData = []
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

        train_data = data_split(df_processed, train_start.date(), train_end.date())
        val_data = data_split(df_processed, val_start.date(), val_end.date())
        trade_data = data_split(df_processed, trade_start.date(), trade_end.date())

        trainData.append(train_data)
        valData.append(val_data)
        tradeData.append(trade_data)

    # lookback_days  0:
    # df_daily = df_daily.iloc[lookback_days:].reset_index(drop=True)
    print(len(tradeData))
    print (f"{tradeData[0]}")

# Trade date including the extra 60 days
#           date      open      high  ...        volume      tic   day
# 0   2020-11-05  14144.01  15750.00  ...  1.437415e+05  BTC-USD  1039
# 0   2020-11-05    402.50    420.40  ...  1.475140e+06  ETH-USD  1039
# 1   2020-11-06  15590.02  15960.00  ...  1.226182e+05  BTC-USD  1040
# 1   2020-11-06    416.73    458.27  ...  1.682441e+06  ETH-USD  1040
# 2   2020-11-07  15579.93  15753.52  ...  1.014312e+05  BTC-USD  1041
# ..         ...       ...       ...  ...           ...      ...   ...
# 115 2021-02-28   1458.27   1468.75  ...  1.410208e+06  ETH-USD  1154

# window dates:

#  Window Train Start  Train End  Val Start    Val End Trade Start  Trade End
#       1  2020-05-04 2020-11-03 2020-09-05 2021-01-03  2020-11-05 2021-03-03
#       2  2020-07-04 2021-01-03 2020-11-05 2021-03-03  2021-01-03 2021-05-03
#       3  2020-09-04 2021-03-03 2021-01-03 2021-05-03  2021-03-05 2021-07-03
#       4  2020-11-04 2021-05-03 2021-03-05 2021-07-03  2021-05-05 2021-09-03
#       5  2021-01-04 2021-07-03 2021-05-05 2021-09-03  2021-07-06 2021-11-03
#       6  2021-03-04 2021-09-03 2021-07-06 2021-11-03  2021-09-05 2022-01-03
#       7  2021-05-04 2021-11-03 2021-09-05 2022-01-03  2021-11-05 2022-03-03
#       8  2021-07-04 2022-01-03 2021-11-05 2022-03-03  2022-01-03 2022-05-03
#       9  2021-09-04 2022-03-03 2022-01-03 2022-05-03  2022-03-05 2022-07-03
#      10  2021-11-04 2022-05-03 2022-03-05 2022-07-03  2022-05-05 2022-09-03
#      11  2022-01-04 2022-07-03 2022-05-05 2022-09-03  2022-07-06 2022-11-03
#      12  2022-03-04 2022-09-03 2022-07-06 2022-11-03  2022-09-05 2023-01-03
#      13  2022-05-04 2022-11-03 2022-09-05 2023-01-03  2022-11-05 2023-03-03
#      14  2022-07-04 2023-01-03 2022-11-05 2023-03-03  2023-01-03 2023-05-03
#      15  2022-09-04 2023-03-03 2023-01-03 2023-05-03  2023-03-05 2023-07-03
#      16  2022-11-04 2023-05-03 2023-03-05 2023-07-03  2023-05-05 2023-09-03
#      17  2023-01-04 2023-07-03 2023-05-05 2023-09-03  2023-07-06 2023-11-03
#      18  2023-03-04 2023-09-03 2023-07-06 2023-11-03  2023-09-05 2024-01-03
#      19  2023-05-04 2023-11-03 2023-09-05 2024-01-03  2023-11-05 2024-03-03
#      20  2023-07-04 2024-01-03 2023-11-05 2024-03-03  2024-01-04 2024-05-03
#      21  2023-09-04 2024-03-03 2024-01-04 2024-05-03  2024-03-05 2024-07-03
#      22  2023-11-04 2024-05-03 2024-03-05 2024-07-03  2024-05-05 2024-09-03
#      23  2024-01-04 2024-07-03 2024-05-05 2024-09-03  2024-07-06 2024-11-03
#      24  2024-03-04 2024-09-03 2024-07-06 2024-11-03  2024-09-05 2025-01-03
#      25  2024-05-04 2024-11-03 2024-09-05 2025-01-03  2024-11-05 2025-03-03
#      26  2024-07-04 2025-01-03 2024-11-05 2025-03-03  2025-01-03 2025-05-03

Dates for windows is:
 Window Train Start  Train End  Val Start    Val End Trade Start  Trade End
      1  2020-05-04 2020-11-03 2020-09-05 2021-01-03  2020-11-05 2021-03-03

The data split starts from the correct date (day 1039 aligns with 2020-11-05 from the first start_date as 2020-05-04) as below: 
          date      open      high  ...        volume      tic   day
0   2020-11-05  14144.01  15750.00  ...  1.437415e+05  BTC-USD  1039
0   2020-11-05    402.50    420.40  ...  1.475140e+06  ETH-USD  1039

However the account values start recording from: 2021-03-02.
Is this a bug in the model.DRL_prediction ? or what else could be the couse of it?