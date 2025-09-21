import pandas as pd
from dateutil.relativedelta import relativedelta
 

from finrl.config import TRAIN_START_DATE, TRADE_END_DATE
from dateutil.relativedelta import relativedelta
import pandas as pd

def get_rolling_windows(train_months=2, val_months=1, trade_months=1, 
                        start_date_str=TRAIN_START_DATE, 
                        end_date_str=TRADE_END_DATE,
                        next_rollings_months=0):

    start_date = pd.to_datetime(start_date_str)
    end_date = pd.to_datetime(end_date_str)

    # Define validation/trade durations as months 
    val_duration   = relativedelta(months=val_months)   
    trade_duration = relativedelta(months=trade_months) 

    windows = []
    while start_date + relativedelta(months=train_months) + val_duration + trade_duration <= end_date:
        # Training window
        train_start = start_date
        train_end   = train_start + relativedelta(months=train_months) - pd.Timedelta(days=1)

        # Validation
        val_start = train_end + pd.Timedelta(days=1)
        val_end   = val_start + val_duration - pd.Timedelta(days=1)

        # Trading
        trade_start = val_end + pd.Timedelta(days=1)
        trade_end   = trade_start + trade_duration - pd.Timedelta(days=1)

        windows.append((train_start, train_end, val_start, val_end, trade_start, trade_end))

        # Slide start_date forward for next rolling window 
        start_date += relativedelta(months=next_rollings_months)

    print(f"Created {len(windows)} rolling windows.")
    return windows
