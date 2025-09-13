# directory
from __future__ import annotations

DATA_SAVE_DIR = "datasets"
TRAINED_MODEL_DIR = "trained_models"
TENSORBOARD_LOG_DIR = "tensorboard_log"
RESULTS_DIR = "results"

# Full historical training
# TRAIN_START_DATE = "2018-05-07"  
# TRAIN_END_DATE   = "2021-12-31"

# # Validation period (hold-out test)
# TEST_START_DATE  = "2022-01-01"
# TEST_END_DATE    = "2022-12-31"

# # Simulated deployment (trading)
# TRADE_START_DATE = "2023-01-01"
# TRADE_END_DATE   = "2023-12-31"

#60 days overlap onlly to use for features, not scoring
TRAIN_START_DATE = "2020-05-04"  
TRAIN_END_DATE = "2023-04-29"   

TEST_START_DATE = "2023-04-30" 
TEST_END_DATE = "2024-05-31"

TRADE_START_DATE = "2024-06-01"
TRADE_END_DATE = "2025-05-31"

# LOOKBACK_DAYS= 30 # 45
VOLATILITY= 14 #21

LOOKBACK_DAYS= 60

Turbulence_lookback_Train=60
Turbulence_lookback_Val=60
Turbulence_lookback_Trade=60
Volatility_Window_Train=30
Volatility_Window_Val=30
Volatility_Window_Trade=14


TRAIN_LEN = 6
VAL_LEN = 2
TRADE_LEN = 2



#| Phase      | Period Length | Turbulence_lookback | Volatility_Window_TRain |
#| ---------- | ------------- | -------------------------- | ----------------- |
# | Train      | \~1090 days   | 60                         | 30                |
# | Validation | \~397 days    | 60                         | 30                |
# | Trade      | \~365 days    | 30–45                      | 14–21             |



# train_months=6
# val_months=2
# trade_months=2

INDICATORS = [
    "macd",
    "boll_ub",
    "boll_lb",
    "rsi_30",
    "cci_30",
    "adx_30",
    "close_30_sma",
    "close_60_sma",
]




# Model Parameters
# model_configs = {
#     "A2C": {
#         "n_steps": 128, "ent_coef": 0.005, "learning_rate": 0.0005
#     },
#     "PPO": {
#         "ent_coef": 0.01, "n_steps": 2048, "learning_rate": 0.00025, "batch_size": 128
#     },
#     "DDPG": {
#         "buffer_size": 20000, "learning_rate": 0.0001, "batch_size": 128
#     }
# }

model_configs = {
    "A2C": {
        "n_steps": 5, "ent_coef": 0.0, "learning_rate": 0.0007
    },
    "PPO": {
        "ent_coef": 0.01, "n_steps": 2048, "learning_rate": 0.00025, "batch_size": 128
    },
    "DDPG": {
        "buffer_size": 10000, "learning_rate": 0.0005, "batch_size": 64
    }
}


A2C_PARAMS = {"n_steps": 5, "ent_coef": 0.01, "learning_rate": 0.0007}
PPO_PARAMS = {
    "n_steps": 2048,
    "ent_coef": 0.01,
    "learning_rate": 0.00025,
    "batch_size": 64,
}
DDPG_PARAMS = {"batch_size": 128, "buffer_size": 50000, "learning_rate": 0.001}
TD3_PARAMS = {"batch_size": 100, "buffer_size": 1000000, "learning_rate": 0.001}
SAC_PARAMS = {
    "batch_size": 64,
    "buffer_size": 100000,
    "learning_rate": 0.0001,
    "learning_starts": 100,
    "ent_coef": "auto_0.1",
}
ERL_PARAMS = {
    "learning_rate": 3e-5,
    "batch_size": 2048,
    "gamma": 0.985,
    "seed": 312,
    "net_dimension": 512,
    "target_step": 5000,
    "eval_gap": 30,
    "eval_times": 64,  # bug fix:KeyError: 'eval_times' line 68, in get_model model.eval_times = model_kwargs["eval_times"]
}
RLlib_PARAMS = {"lr": 5e-5, "train_batch_size": 500, "gamma": 0.99}


# Possible time zones
TIME_ZONE_SHANGHAI = "Asia/Shanghai"  # Hang Seng HSI, SSE, CSI
TIME_ZONE_USEASTERN = "US/Eastern"  # Dow, Nasdaq, SP
TIME_ZONE_PARIS = "Europe/Paris"  # CAC,
TIME_ZONE_BERLIN = "Europe/Berlin"  # DAX, TECDAX, MDAX, SDAX
TIME_ZONE_JAKARTA = "Asia/Jakarta"  # LQ45
TIME_ZONE_SELFDEFINED = "xxx"  # If neither of the above is your time zone, you should define it, and set USE_TIME_ZONE_SELFDEFINED 1.
USE_TIME_ZONE_SELFDEFINED = 0  # 0 (default) or 1 (use the self defined)

# parameters for data sources
ALPACA_API_KEY = "xxx"  # your ALPACA_API_KEY
ALPACA_API_SECRET = "xxx"  # your ALPACA_API_SECRET
ALPACA_API_BASE_URL = "https://paper-api.alpaca.markets"  # alpaca url
BINANCE_BASE_URL = "https://data.binance.vision/"  # binance url
