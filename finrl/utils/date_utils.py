import pandas as pd
from finrl.config import LOOKBACK_DAYS, TRAIN_LEN, VAL_LEN,TRADE_LEN

def adjust_window_dates(train_start, train_end, val_start, val_end, trade_start, trade_end,
                        lookback_days=LOOKBACK_DAYS,
                        train_len=TRAIN_LEN,
                        val_len=VAL_LEN,
                        trade_len=TRADE_LEN):
    """
    Adjusts window dates so that the returned dates reflect 
    the *actual* trading and validation start after warm-up days.
    
    Returns:
        list of shifted dates: [train_start, train_end, val_start, val_end, trade_start, trade_end]
    """
    # Ensure pandas Timestamp
    train_start = pd.Timestamp(train_start)
    train_end   = pd.Timestamp(train_end)
    val_start   = pd.Timestamp(val_start)
    val_end     = pd.Timestamp(val_end)
    trade_start = pd.Timestamp(trade_start)
    trade_end   = pd.Timestamp(trade_end)
    
    # Adjust train end if needed (typically leave as-is)
    shifted_train_end = train_end
    
    # Shift validation start
    shifted_val_start = val_start + pd.Timedelta(days=lookback_days - 1)
    
    # Keep validation end (still based on months)
    shifted_val_end = val_end
    
    # Shift trade start to skip warm-up
    shifted_trade_start = trade_start + pd.Timedelta(days=lookback_days - 1)
    
    # Keep trade end (based on months)
    shifted_trade_end = trade_end
    
    return [
        train_start.date(),
        shifted_train_end.date(),
        shifted_val_start.date(),
        shifted_val_end.date(),
        shifted_trade_start.date(),
        shifted_trade_end.date()
    ]

