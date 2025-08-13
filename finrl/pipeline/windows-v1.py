
import pandas as pd
import numpy as np
import os
from stable_baselines3.common.vec_env import DummyVecEnv
from finrl.pipeline.plot_values import plot_dashboard #plot_account_values, plot_counts_rewards, plot_volatility_return, plot_sharp_window
from finrl.meta.preprocessor.preprocessors import FeatureEngineer, data_split
from finrl.meta.env_crypto_trading.env_cryptotrading import CryptoTradingEnv
from finrl.agents.stablebaselines3.models import DRLAgent
from finrl.plot.plot import get_daily_return  
from finrl.config import model_configs


def run_training_windows(windows, df_processed, results_path):
   
    val_results_path = os.path.join(results_path, "validation_metrix.csv")
    trade_results_path = os.path.join(results_path, "trading_metrix.csv")
    daily_accounts_path = os.path.join(results_path, "account_values.csv")

    performance_log = []
    val_report_metrics = []

    PPO_model_kwargs = model_configs["PPO"]
    A2C_model_kwargs = model_configs["A2C"]
    DDPG_model_kwargs = model_configs["DDPG"]


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
        # val_sharpe_dict = {name: sharpe for name, sharpe in val_sharpes}

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
                    })
        else:
            print(f"❌ No valid model selected in window {i+1} — skipping trade step.")


            #  --- Trade End ---

            print(f"✅ Window {i+1} Summary:")
            print(f"  🔹 Train Dates : {train_start.date()} → {train_end.date()}")
            print(f"  🔹 Trade Dates : {val_end.date()} → {trade_end.date()}")
            print(f"  🔹 Best Model  : {best_model.__class__.__name__ if best_model else 'None'}")
            print(f"  🔹 Sharpe      : {best_sharpe:.2f}")
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


    # if not account_values_df.empty:
    #     plot_account_values(account_values_df)
    #     plot_counts_rewards(account_values_df)
    # else:
    #     print("No results to plot.")

    # if not df_metrics.empty:
    #     plot_volatility_return(df_metrics)
    #     plot_sharp_window(df_metrics)
    # else:
    #     print("No results to plot.")

   

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

        plot_dashboard(account_values_df, df_metrics)


        df_metrics.to_csv(trade_results_path, index=False)
        print(f"Trade Metrics saved to", {trade_results_path})


        # df_account_values_daily = pd.DataFrame(account_values_df)
        account_values_df.to_csv(daily_accounts_path, index=False)
        print(f"Daily account values saved to", {daily_accounts_path})
        
    else:
        print("No results to analyze.")

