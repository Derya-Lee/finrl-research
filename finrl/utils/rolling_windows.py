import pandas as pd
from dateutil.relativedelta import relativedelta
from finrl.config import LOOKBACK_DAYS, TRAIN_LEN, VAL_LEN,TRADE_LEN
 

from finrl.config import TRAIN_START_DATE, TRADE_END_DATE
# def get_rolling_windows(train_months=6, val_months=2, trade_months=2, start_date_str=TRAIN_START_DATE, end_date_str=TRADE_END_DATE):
#     start_date = pd.to_datetime(start_date_str)
#     end_date = pd.to_datetime(end_date_str)
    
#     print(f" train_months {train_months} ")
#     windows = []
#     while start_date + relativedelta(months=train_months + val_months + trade_months) <= end_date:
#         train_start = start_date
#         train_end = train_start + relativedelta(months=train_months)
#         val_start = train_end + relativedelta(days=1)
#         val_end = train_end + relativedelta(months=val_months)
#         trade_start = val_end + relativedelta(days=1)
#         trade_end = val_end + relativedelta(months=trade_months)

#         windows.append((train_start, train_end, val_start, val_end, trade_start, trade_end))
#         start_date += relativedelta(months=3)

#     print(f" Created {len(windows)} rolling windows.")
#     return windows


def get_rolling_windows(train_months=TRAIN_LEN, val_months=2, trade_months=2, 
                        start_date_str=TRAIN_START_DATE, 
                        end_date_str=TRADE_END_DATE,
                        lookback_days=LOOKBACK_DAYS):

    start_date = pd.to_datetime(start_date_str)
    end_date = pd.to_datetime(end_date_str)

    windows = []
    while start_date + relativedelta(months=train_months + val_months + trade_months) <= end_date:
        train_start = start_date
        train_end = train_start + relativedelta(months=train_months) - pd.Timedelta(days=1)

        # Shift val_start back by lookback_days (but not before train_start)
        val_start = max(train_end - pd.Timedelta(days=lookback_days-1), train_start)
        val_end = train_end + relativedelta(months=VAL_LEN)

        # Shift trade_start back by lookback_days (but not before val_start)
        trade_start = max(val_end - pd.Timedelta(days=lookback_days-1), val_start)
        trade_end = val_end + relativedelta(months=TRADE_LEN)

        windows.append((train_start, train_end, val_start, val_end, trade_start, trade_end))

        # Slide start_date forward for next rolling window ( TODO observe 'is more windows better' )
        start_date += relativedelta(months=2)

    print(f"Created {len(windows)} rolling windows.")
    return windows
