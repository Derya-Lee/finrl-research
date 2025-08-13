import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import datetime
# import warnings


# from dateutil.relativedelta import relativedelta
from finrl.utils.rolling_windows import get_rolling_windows
from finrl.meta.preprocessor.preprocessors import FeatureEngineer, data_split
from finrl.meta.preprocessor.binancedownloader import BinanceDownloader
from stable_baselines3 import PPO, A2C, DDPG
from stable_baselines3.common.vec_env import DummyVecEnv
from finrl.meta.preprocessor.binancedownloader import BinanceDownloader
from finrl.meta.preprocessor.preprocessors import FeatureEngineer, data_split
from finrl.meta.env_crypto_trading.env_cryptotrading import CryptoTradingEnv
from finrl.agents.stablebaselines3.models import DRLAgent
from finrl.plot.plot import get_daily_return  


def test_deterministic_process() : 
    import os

    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, "data")
    results_path = os.path.join(current_dir, "results")
    file_name = "binance_data_raw.csv"
    dt_raw_path = os.path.join(data_path, file_name)
    dt_processed_path = os.path.join(data_path, "processed_bnc_data.csv")
    val_results_path = os.path.join(results_path, "validation_metrix.csv")
    trade_results_path = os.path.join(results_path, "trading_metrix.csv")
    daily_accounts_path = os.path.join(results_path, "account_values.csv")
    
    tickers = ["BTCUSDT", "ETHUSDT"]
    bd = BinanceDownloader()

    # if os.path.exists(dt_raw_path):
    #     # Download again if changing dates
    #     print(" Loading Binance data from local cache...")
    #     df_raw = pd.read_csv(dt_raw_path, parse_dates=["date"])
    #     print(f"df_raw", {len(df_raw["date"])})
    #     print(f"df_raw unique", {len(df_raw["date"].unique())})
    #     print("Data retrieved from:", data_path)
    # else:
    df_raw = bd.download_multiple(ticker_list=tickers, start_str="1 Jan, 2018")
    df_raw.to_csv(dt_raw_path, index=False)
    print("Data saved to:", data_path)

    A2C_model_kwargs = { 'n_steps': 5, 'ent_coef': 0.005, 'learning_rate': 0.0007}
    PPO_model_kwargs = { 'ent_coef': 0.01, 'n_steps': 2048, 'learning_rate': 0.00025, 'batch_size': 128}
    DDPG_model_kwargs = { 'buffer_size': 10000, 'learning_rate': 0.0005, 'batch_size': 64}
    fe = FeatureEngineer(use_technical_indicator=True,
                        tech_indicator_list=["macd", "rsi_30", "cci_30"], 
                        use_vix=False,
                        use_turbulence=True)

    df_processed = fe.preprocess_data(df_raw) 
    if os.path.exists(data_path):
         df_processed.to_csv(dt_processed_path, index=False)

    start_date = pd.Timestamp("2021-01-01")
    end_date = start_date + pd.DateOffset(days=360)

    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    # should be Start: 2021-01-01, End: 2021-06-30
    print(f"Start: {start_date_str}, End: {end_date_str}")

    windows = get_rolling_windows(
        train_months=1,
        val_months=1,
        trade_months=1,
        start_date_str=start_date_str ,
        end_date_str=end_date_str
    )
    val_report_metrics = []
    account_values_dict = {} # account_values 
    performance_log = []
# train_start, train_end, val_start, val_end, trade_start, trade_end, windows, df_processed, 
    for i, (train_start, train_end, val_start, val_end, trade_start, trade_end) in enumerate(windows):
        train_data = data_split(df_processed, train_start, train_end)
        val_data = data_split(df_processed, val_start, val_end)
        trade_data = data_split(df_processed, trade_start, trade_end)
        min_days_required = 30
        
        window_name = f"window_{i+1}"
        print(f" Rolling {window_name}: {train_start.date()} to {trade_end.date()}")

        env_train = DummyVecEnv([lambda: CryptoTradingEnv(train_data)])
        agent = DRLAgent(env=env_train)

        models = {
            "ppo": agent.train_PPO(total_timesteps=len(train_data)*30, model_kwargs=PPO_model_kwargs),
            "a2c": agent.train_A2C(total_timesteps=len(train_data)*30, model_kwargs=A2C_model_kwargs),
            "ddpg": agent.train_DDPG(total_timesteps=int(len(train_data)*30*0.5), model_kwargs=DDPG_model_kwargs)
        }

        best_model = None
        best_sharpe = -np.inf
        val_sharpes = []
        val_report = []

        for name, model in models.items():
            env_val = DummyVecEnv([lambda: CryptoTradingEnv(val_data)])
            sharpe_metrics = DRLAgent.DRL_evaluation(model=model, environment=env_val)
            sharpe = sharpe_metrics["sharpe"]
            val_sharpes.append({"name": name, "sharpe": sharpe})
            # account_vals = env_val.envs[0].asset_memory

            if not np.isnan(sharpe) and sharpe > best_sharpe:
                best_model = model
                best_sharpe = sharpe     

        #  --- Trade start ---
        env_trade = DummyVecEnv([lambda: CryptoTradingEnv(trade_data)])
        
        # Sharpe/volatility during validation can be compared against to the actual during training
        val_sharpe_dict = {name: sharpe for name, sharpe in val_sharpes}

        if best_model is not None:
                startdt = pd.to_datetime(trade_start)
                env_trade.envs[0].trading_mode = True
                df_result = DRLAgent.DRL_prediction(model=best_model, environment=env_trade, start_date=startdt)

                df_result["window"] = i + 1
                
                # concat for reporting
                if "account_values_df" not in locals():
                    account_values_df = df_result.copy()
                else:
                    account_values_df = pd.concat([account_values_df, df_result], ignore_index=True)

                daily_retun_values_df = df_result[["date", "account_value"]].copy()
                # daily_retun_values_df["date"] = pd.to_datetime(daily_retun_values_df["date"])
                # daily_retun_values_df.set_index("date", inplace=True)
                account_values = daily_retun_values_df["account_value"]

                daily_returns = get_daily_return(daily_retun_values_df)       
                sharpe = (365**0.5) * daily_returns.mean() / daily_returns.std()      
                # sharpe = df_result["sharpe"]
                total_return = account_values.iloc[-1] / account_values.iloc[0] - 1
                volatility = daily_returns.std()
                max_drawdown = (account_values.cummax() - account_values).max() / account_values.cummax().max()

                # print(f"account_values {account_values}")
                # print(f"account_values.iloc[0] {account_values.iloc[0]}")

                # expected_days = len(env.df.date.unique())
                # print(len(account_values), expected_days)
                


                performance_log.append({
                        "agent": best_model.__class__.__name__,
                        "window": i + 1,
                        "train_start": train_start.date(),
                        "train_end": train_end.date(),
                        "trade_start": trade_start.date(),
                        "trade_end": trade_end.date(),
                        "sharpe_ratio": sharpe,
                        "min_account_value": account_values.min(),
                        "max_account_value": account_values.max(),
                        "total_return": total_return,
                        "volatility (std)": volatility,
                        "max_drawdown": max_drawdown,
                        "initial_acc_val": account_values.iloc[0],
                        "final_acc_val": account_values.iloc[-1]
                        # **val_sharpe_dict
                    })
        else:
            print(f"❌ No valid model selected in window {i+1} — skipping trade step.")


         #  --- Trade End ---

         #  --- validation data reporting ---
        val_report = {
            "agent": best_model.__class__.__name__,
            "window": i + 1,
            "train_start": train_start.date(),
            "train_end": train_end.date(),
            "val_start": val_start,
            "val_end": val_end,
        }

        for sharpe_entry in val_sharpes:
            model_name = sharpe_entry["name"]
            val_report[f"{model_name}_sharpe"] = sharpe_entry["sharpe"]

        val_report_metrics.append(val_report)

    if val_report_metrics:
        val_metrics = pd.DataFrame(val_report_metrics)
        val_metrics.to_csv(val_results_path, index=False)
        print(f"Metrics saved to", {val_results_path})
        # display(val_report_metrics) - look for import matplotlib.pyplot as plt

    else:
        print("No validation report to analyze.")

    #  --- END - validation data reporting ---

    if performance_log:
        df_metrics = pd.DataFrame(performance_log)
        df_metrics.to_csv(trade_results_path, index=False)
        print(f"Trade Metrics saved to", {trade_results_path})
   

        df_account_values_daily = pd.DataFrame(account_values_df)
        df_account_values_daily.to_csv(daily_accounts_path, index=False)
        print(f"Daily account values saved to", {daily_accounts_path})
        
    else:
        print("No results to analyze.")
  
