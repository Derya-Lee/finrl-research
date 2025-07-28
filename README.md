## 📈 Ensemble Strategy for Cryptocurrency Trading Using Deep Reinforcement Learning

This project implements a rolling-window **ensemble strategy** for trading cryptocurrencies using **Deep Reinforcement Learning (DRL)**. It is adapted from the paper:  
📄 *"Deep Reinforcement Learning for Automated Stock Trading: An Ensemble Strategy" (Liu et al., 2020)*.

The strategy trains and evaluates three DRL agents:
- 🟦 PPO (Proximal Policy Optimization)
- 🟨 A2C (Advantage Actor-Critic)
- 🟥 DDPG (Deep Deterministic Policy Gradient)

Each agent is retrained in a rolling-window framework and evaluated based on **Sharpe ratio** during a validation window. The best-performing agent is used to trade in the following period.

---

### 📊 Rolling Window Evaluation

Each rolling window follows this structure:

- **Training**: 6 months  
- **Validation**: 2 months  
- **Trading**: 2 months  
- Then the window advances by 3 months.

---

## 📄 Sample: `results/crypto_metrics.csv`

This file stores key evaluation metrics for each agent per rolling window, such as Sharpe ratio, returns, and drawdown.

```csv
agent,window,train_start,train_end,trade_start,trade_end,sharpe_ratio,total_return,volatility,max_drawdown,final_account_value,asset_class
DDPG,1,2020-05-04,2020-11-04,2021-01-04,2021-03-04,0.5327,0.4121,0.0832,0.1289,1411847.68,Crypto
A2C,1,2020-05-04,2020-11-04,2021-01-04,2021-03-04,0.4795,0.3421,0.0785,0.1353,1342186.71,Crypto
PPO,1,2020-05-04,2020-11-04,2021-01-04,2021-03-04,0.4228,0.3185,0.0752,0.1445,1319852.64,Crypto
DDPG,2,2020-08-04,2021-02-04,2021-04-04,2021-06-04,0.5893,0.4578,0.0923,0.1171,1483294.10,Crypto
A2C,2,2020-08-04,2021-02-04,2021-04-04,2021-06-04,0.4386,0.3789,0.0854,0.1256,1371625.35,Crypto
PPO,2,2020-08-04,2021-02-04,2021-04-04,2021-06-04,0.4012,0.3124,0.0816,0.1323,1298154.76,Crypto


### ✅ Results Summary (Sample Output)

```plaintext
Window 1
  Train window: 2020-05-04 to 2020-11-04 — 184 days
  Val window  : 2020-11-04 to 2021-01-04 — 61 days
  Trade window: 2021-01-04 to 2021-03-04 — 59 days
Using cpu device
🔍 Sample PPO action: [[-0.1863538  -0.20843586]]

📊 PPO Account Value Range: 1000000.00 to 1411847.68
📈 PPO Sharpe Ratio: 0.4228

📊 A2C Account Value Range: 1000000.00 to 1342186.71
📈 A2C Sharpe Ratio: 0.4795

📊 DDPG Account Value Range: 1000000.00 to 1387321.11
📈 DDPG Sharpe Ratio: 0.5327

🏆 Best model: DDPG with Sharpe 0.5327
✅ Results saved to: `results/crypto_account_values.csv`
