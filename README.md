# FinRL Research Guide

This repository contains experiments and analysis conducted for the dissertation project on AI-driven trading systems.  
It adapts and extends components of the **FinRL (refactored)** library for cryptocurrency trading research, with a focus on risk-aware and sentiment-aware feature integration.  

**source used**
https://github.com/AI4Finance-Foundation/FinRL/tree/master


**To set your environment**
Either use requirements_min.txt for minimal requirements or the full version requirements.txt 
---

## 📂 Project Structure

### 1. `Data/`
Input datasets used for both example runs and main experiments.

- **Example experiments (input data)**
  - `binance_data_raw_example.csv` → raw input
  - `example_processed_bnc_data.csv` → processed OHLCV data
  - `example_sentiment_bnc_data.csv` → sentiment features
  - `example_voltur_bnc_data.csv` → volatility & turbulence features  

- **Main experiments (input data)**
  - `binance_data_raw.csv` → raw input
  - `processed_bnc_data.csv` → processed OHLCV data
  - `sentiment_bnc_data.csv` → sentiment features
  - `voltur_bnc_data.csv` → volatility & turbulence features  

---

### 2. `notebooks/`  
Jupyter notebooks for experiments and data analysis.  

- **Example (short runs)**  
  - `ensemble_research_short.ipynb` → reduced settings for testing experiment parameters (dates, window length, etc.)  

- **Main notebooks**  
  - `ensemble_research.ipynb` → full experiment runs, dissertation results  
  - `data_analysis.ipynb` → descriptive and statistical analysis of experiment results  

---

### 3. `port_DRL_exp/`  
Customized FinRL implementation for this project.  
Only relevant modified files are listed here. Files not listed are unchanged and included for completeness/future extensions.  

#### a. `agents/stablebaseline3/models.py`
- Contains **agent definitions** and functions for:
  - `DRL_evaluation` (Phase 2 & 3): resets environment, runs trading over each window, calculates Sharpe ratio from total asset trajectory.  
  - `DRL_prediction`: applies trained model to test windows, records daily results.  

Trading process:  
- Reset → unique environment per window.  
- Each day: agent decides {buy, sell, hold} → executed on available cash & holdings.  
- Asset trajectory recorded → performance metrics calculated.  

---

#### b. `meta/env_crypto_trading/env_cryptotrading.py`
**Environment logic.**  

- **State**:  
  - Always includes `cash + holdings (by token)`  
  - Adds volatility & turbulence (Experiment 2) or sentiment (Experiment 3)  
  - For baseline (Experiment 1): state includes OHLCV features only.  

- **Step() function**:  
  - Chooses action (buy/sell/hold) per token  
  - Executes trade, updates cash and holdings  
  - Calculates reward for the day  
  - Updates total asset = cash + mark-to-market holdings  

⚠️ Hardcoded features ensure research clarity (less flexible than original FinRL, but avoids unintended inputs).  

---

#### c. `meta/preprocessors/`
- `binancedownloader.py` → downloads Binance OHLCV data  
- `preprocessors.py` → modified `FeatureEngineer` for crypto:  
  - Cleans data (fills missing, factorizes dates)  
  - Integrates Fear & Greed data  
  - ⚠️ Technical indicators not included (out of scope)  

---

#### d. `utils/`
Helper functions for analysis and evaluation.  

- `calculate_turbulence_crypto.py` → turbulence index (Mahalanobis distance, rolling lookback)  
- `compute_sharpe_metrics.py` → Sharpe ratio calculation  
- `compute_sortino_ratio.py` → Sortino ratio calculation  
- `daily_returns.py` → return calculation  
- `fear_and_greed.py` → sentiment preprocessing  
- `rolling_windows.py` → splits data into rolling windows  
- `sentiment_scores.py` → maps raw Fear & Greed to categories  

- `config.py` → experiment settings (date ranges, agents, hyperparameters)  

---

### 4. `Report/`  
Helper data and functions for descriptive and regre
