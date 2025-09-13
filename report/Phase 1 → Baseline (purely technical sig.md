Phase 1 → Baseline (purely technical signals).

Phase 2 → Risk-aware features (volatility, turbulence).

Phase 3 → Sentiment-aware features.

Data Preperation and Description

date

window (rolling window ID)

account_value

volatility (phase 2+)

turbulence (phase 2+)

fear_greed (phase 3)

2. Descriptive Statistics

# Summary stats
print(df[["account_value", "daily_return", "volatility", "turbulence"]].describe())

# Correlation matrix
print(df[["daily_return", "volatility", "turbulence"]].corr())

reward (daily return):
df["daily_return"] → gives you a series of step-by-step daily returns (each day’s percentage change).

DESCRIBING DATA AND THE STRUCTURE ? OF ANALYSIS

Phase 1 only has account_value and daily_return information. No volatility, turbulence, or sentiment features exist; it is used as control group providing report performance (Sharpe, Sortino, max drawdown, etc.)


Phase 2 and Phase 3 are the risk-aware and sentiment-aware variations of Phase 1 provided with explanatory variables volatility & turbulence and fear_greed features respectively; these phases are used to run descriptive stats, correlations, regressions.

A phase is made up of windows, representing repetetion of the experiment (train - validate - trade circle) for different time frames 



<!-- ( WHY: this is to avoid luck or coincidential results
* can explain with example with a window good results & bad results, what would the results would be...
)  -->

Analysis of Window level results:

each window treated independently to comparin conditions ( turbulence & volatility or sentiment).

# Compute descriptive stats, correlations, regressions within each window.

normalized
df["fear_greed_norm"] = (df["fear_greed"] - 50) / 50

mapped version is =
   -2, <= 24: extreme fear
   -1,  <= 49: fear
    1, <= 74: greed
    2,   extreme greed


Explain meanings :
pair (e.g. reward ~ volatility, reward ~ turbulence, volatility ~ turbulence)

value (the correlation coefficient)

## TODO
generate auto install file for all reqs, ie:
pip install statsmodels


Ensemble (main paper) used:
Sharpe ratio (main metric)
Annualized return & volatility
Profit/loss
Profitability ratio
Sortino ratio
Maximum drawdown (value and duration)

Standard deviation of daily returns reflects volatility.
Annualized volatility
daily_returns.std() * np.sqrt(252)

reward: daily return
Headers on row 2, and data starting from row 3
Column I: window
Column L: account_value-mean
Column M: account_value-std
Column S: reward-mean
Column T: reward-std

sheet name: Control_Group

=((365)^2)*('Sen-Mapped-Daily'!S3/'Sen-Mapped-Daily'!T3)
            'Sen-Norm-Daily'!T3
            'Vol&Tur-Daily'!T3
            Control_Group!T3

=(Control_Group!AH3/Control_Group!AG3) - 1

=DIVIDE('Vol&Tur-Daily'!AA3,'Vol&Tur-Daily'!Z3)-1

=DIVIDE('Sen-Mapped-Daily'!AA3,'Sen-Mapped-Daily'!Z3)-1

=('Vol&Tur-Daily'!R3-'Vol&Tur-Daily'!N3)/'Vol&Tur-Daily'!R3

=('Sen-Norm'!R3-'Sen-Norm-Daily'!N3)/'Sen-Norm-Daily'!R3
=('Sen-Mapped'!R3-'Sen-Mapped-Daily'!N3)/'Sen-Mapped-Daily'!R3


(DIVIDE('Vol&Tur'!A03,'Vol&Tur'!AN3)^(365/'Vol&Tur'!K3))-1

(DIVIDE('Sen-Mapped'!AA3,'Sen-Mapped'!Z3)^(365/'Sen-Mapped'!K3))-1

nnualized volatility or Daily volatility analysis ie. REGRESSION
Annualized volatility is typically more informative in models that assess risk-adjusted returns or overall market instability. If you want to compare the agent's performance over a longer time horizon, it's a good idea to use annualized volatility because it helps normalize for different time periods.

Daily volatility (unannualized) is more granular and is used when you want to assess short-term risk in a specific time window. If your model is highly sensitive to short-term fluctuations, you would use daily volatility instead.

** how an agent's daily or weekly returns are influenced by volatility:
    use annualized volatility to make the results comparable over time.

** NOT USING Daily Volatility, because
    If your analysis is focused on short-term prediction (e.g., within a day or week), daily volatility can provide more relevant insights into how the agent reacts to market fluctuations.


    (using google sheets, or LibreOffice

    =(SQRT(365))*(Control_Group!S3/Control_Group!T3)



IF(G4<=24, "extreme fear", (IF(G4<=49, "fear", IF(G4<=74, "greed", "extreme greed"))))

, also include why I chose Turbulence and not included volatility: After running the individual regressions for phase 1, 2, 3a, and 3b there was nothing to investigate on volatility, but turbulence showed some negative and positive relationship. Volatility was noisy. I am going to repeat the regressions, and add the results before the sentiment effect we just did. 



=FILTER('Vol&Tur Corr'!B2:B67, ('Vol&Tur Corr'!A2:A67=B2) * ('Vol&Tur Corr'!C2:C67=A3))



Explain using both volatility and turbulence together based on correlation
example only:
“Correlations of rewards with volatility and turbulence were weak, indicating limited direct dependence. However, turbulence and volatility themselves were moderately correlated, suggesting they both capture overlapping aspects of market instability. The stability/variability of this relationship across windows is relevant for assessing whether the agent was trained on complementary or redundant signals.”
    

    DO correlations Fear & greed using helper function
    "When the agent saw a continuous sentiment signal, its performance correlations with sentiment remained weak and consistent."

    “When trained on the normalized continuous fear–greed index (Phase 3a), the agent’s reward correlations with sentiment were weakly negative but relatively stable across windows. By contrast, when trained on the discretized mapped version (Phase 3b), the correlations were more variable, with stronger negative medians but wider dispersion. This suggests that discretizing sentiment into categorical regimes introduced additional noise and instability in how the agent’s performance aligned with sentiment, whereas the normalized version offered smoother but weaker associations. However, in both cases the correlations remained low, indicating that sentiment did not strongly drive short-term agent returns.”

    "Sharpe_ann", "Sortino_ann", "Volatility_ann", "Max_Drawdown"



1. Deep Reinforcement Learning (DRL)

How it works: An agent learns to take buy/sell/hold actions in a simulated environment based on maximizing cumulative rewards (e.g., returns or Sharpe ratio).

Popular algorithms:

DQN (Deep Q-Network)

PPO (Proximal Policy Optimization)

A2C/A3C (Advantage Actor Critic)

DDPG (Deep Deterministic Policy Gradient)

Why it's used: Crypto markets are highly stochastic and non-linear, making DRL ideal for modeling them without needing explicit price forecasting.

2. Supervised Machine Learning for Price Prediction

How it works: Historical price/volume/technical indicators are used to predict the next price movement or return.

Popular models:

XGBoost / LightGBM

Random Forest

Support Vector Machines (SVM)

Multi-Layer Perceptrons (MLP)

Usage: These are typically used for classification (e.g., price up/down) or regression (price forecasting), which then inform trading decisions.

3. Deep Learning for Time-Series Forecasting

How it works: Models like LSTM, GRU, or Temporal CNNs are used to learn from sequential data such as candlestick prices and volumes.

Popular models:

LSTM (Long Short-Term Memory)

GRU (Gated Recurrent Units)

Temporal Convolutional Networks (TCNs)

Transformer-based models

Why it’s used: These models are good at capturing temporal dependencies and market trends.

4. Sentiment Analysis + Trading

How it works: NLP techniques are applied to Twitter, Reddit, or news data to gauge market sentiment and make trading decisions.

Popular models:

BERT, RoBERTa, FinBERT

Rule-based sentiment scoring

Combined with supervised ML or DRL strategies

Why it’s used: Crypto prices are highly sensitive to news, influencers (like Elon Musk), and social media.

5. Hybrid Models (Forecasting + Reinforcement Learning)

Some researchers combine supervised forecasting (e.g., LSTM predicting future returns) with RL that decides how much to trade based on the forecast confidence and market conditions.