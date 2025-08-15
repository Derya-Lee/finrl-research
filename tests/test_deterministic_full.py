
import os
import pandas as pd

from finrl.utils.rolling_windows import get_rolling_windows
from finrl.pipeline.windows import run_training_windows
from finrl.meta.preprocessor.preprocessors import FeatureEngineer
from finrl.meta.preprocessor.binancedownloader import BinanceDownloader
from finrl.meta.preprocessor.binancedownloader import BinanceDownloader
from finrl.config import TRAIN_LEN, VAL_LEN, TRADE_LEN, TRAIN_START_DATE, TRADE_END_DATE



def test_deterministic_process() : 

    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, "data")
    results_path = os.path.join(current_dir, "results")
    file_name = "binance_data_raw.csv"
    dt_raw_path = os.path.join(data_path, file_name)
    dt_processed_path = os.path.join(data_path, "processed_bnc_data.csv")
    
    tickers = ["BTCUSDT", "ETHUSDT"]
    bd = BinanceDownloader()

    df_raw = bd.download_multiple(ticker_list=tickers, start_str="1 Jan, 2018")
    df_raw.to_csv(dt_raw_path, index=False)
    print("Data saved to:", data_path)


    fe = FeatureEngineer(use_technical_indicator=False,
                        tech_indicator_list=["macd", "rsi_30", "cci_30"], 
                        use_vix=False,
                        use_turbulence=True)

    df_processed = fe.preprocess_data(df_raw) 
    if os.path.exists(data_path):
         df_processed.to_csv(dt_processed_path, index=False)

    start_date = pd.Timestamp(TRAIN_START_DATE)
    end_date =  pd.Timestamp(TRADE_END_DATE)

    # start_date_str = start_date.strftime("%Y-%m-%d")
    # end_date_str = end_date.strftime("%Y-%m-%d")

    windows = get_rolling_windows(
        train_months=TRAIN_LEN,
        val_months=VAL_LEN,
        trade_months=TRADE_LEN,
        start_date_str=start_date ,
        end_date_str=end_date
    )

    run_training_windows(windows, df_processed, results_path)
