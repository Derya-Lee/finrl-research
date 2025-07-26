import pandas as pd
from dateutil.relativedelta import relativedelta
from finrl.config import TRAIN_START_DATE, TRADE_END_DATE

def get_rolling_windows(train_months=6, val_months=2, trade_months=2):
    start_date = pd.to_datetime(TRAIN_START_DATE)
    end_date = pd.to_datetime(TRADE_END_DATE)

    windows = []
    while start_date + relativedelta(months=train_months + val_months + trade_months) <= end_date:
        train_start = start_date
        train_end = train_start + relativedelta(months=train_months)
        val_end = train_end + relativedelta(months=val_months)
        trade_end = val_end + relativedelta(months=trade_months)

        windows.append((train_start, train_end, val_end, trade_end))
        start_date += relativedelta(months=3)

    print(f"🔄 Created {len(windows)} rolling windows.")
    return windows
