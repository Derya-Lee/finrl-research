TRAIN_START_DATE = "2020-05-04"  
TRADE_END_DATE = "2025-05-31"

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