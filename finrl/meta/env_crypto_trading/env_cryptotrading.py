import numpy as np
import pandas as pd
import gym
from gym import spaces

class CryptoTradingEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    #TODO remove default value crypto_dim=30,
    def __init__(self, df, crypto_dim=30, hmax=100, initial_amount=1e6,
                 buy_cost_pct=0.0001, sell_cost_pct=0.0001, reward_scaling=1e-4,
                 tech_indicator_list=None):
        super(CryptoTradingEnv, self).__init__()

        self.df = df.reset_index(drop=True)
        self.crypto_dim = len(self.df['tic'].unique())
        self.hmax = hmax
        self.initial_amount = initial_amount
        self.buy_cost_pct = buy_cost_pct
        self.sell_cost_pct = sell_cost_pct
        self.reward_scaling = reward_scaling
        self.tech_indicator_list = tech_indicator_list if tech_indicator_list else ['macd', 'rsi_30', 'cci_30']
        self.action_space = spaces.Box(low=-1, high=1, shape=(self.crypto_dim,))
        obs_shape = 1 + 2 * self.crypto_dim + len(self.tech_indicator_list) * self.crypto_dim
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(obs_shape,), dtype=np.float32)
        # self.observation_space = spaces.Box(
        #     low=-np.inf, high=np.inf, shape=(1 + 2 * self.crypto_dim + len(self.tech_indicator_list) * self.crypto_dim,)
        # )

        self.reset()
      
    def reset(self):
        self.day = 0
        self.data = self.df.loc[self.df.date == self.df.date.unique()[self.day]]
        self.terminal = False

        self.cash = self.initial_amount
        self.stocks = np.zeros(self.crypto_dim)  # no holdings at start
        self.total_asset = self.initial_amount
        self.asset_memory = [self.total_asset]

        self.state = [self.total_asset] + \
                    list(self.stocks) + \
                    self.data.close.values.tolist() + \
                    sum([self.data[tech].values.tolist() for tech in self.tech_indicator_list], [])

        return np.array(self.state)

    def step(self, actions):
        self.terminal = self.day >= len(self.df.date.unique()) - 1
        if self.terminal:
            return self.state, self._reward(), self.terminal, {}

        prices = self.data.close.values
        actions = actions * self.hmax

        # === SELL ===
        for i in np.where(actions < 0)[0]:
            sell_amount = min(self.stocks[i], -actions[i])
            self.stocks[i] -= sell_amount
            self.cash += prices[i] * sell_amount * (1 - self.sell_cost_pct)

        # === BUY ===
        for i in np.where(actions > 0)[0]:
            max_buy = self.cash // (prices[i] * (1 + self.buy_cost_pct))
            buy_amount = min(max_buy, actions[i])
            self.stocks[i] += buy_amount
            self.cash -= prices[i] * buy_amount * (1 + self.buy_cost_pct)

        # === Advance to Next Day ===
        self.day += 1
        self.data = self.df.loc[self.df.date == self.df.date.unique()[self.day]]
        prices = self.data.close.values

        prev_asset = self.total_asset
        self.total_asset = self.cash + np.sum(self.stocks * prices)
        reward = (self.total_asset - prev_asset) * self.reward_scaling
        self.asset_memory.append(self.total_asset)

        self.state = [self.total_asset] + \
                    list(self.stocks) + \
                    prices.tolist() + \
                    sum([self.data[tech].values.tolist() for tech in self.tech_indicator_list], [])

        # === Optional Debug Logging ===
       # print(f" Day {self.day} | Cash: {self.cash:.2f} | Stocks: {self.stocks.round(2)} | Asset: {self.total_asset:.2f} | Reward: {reward:.5f}")

        return np.array(self.state), reward, self.terminal, {}


    def _get_total_asset(self):
        return self.state[0]  # simply return current balance (can be expanded)

    def _reward(self):
        return self.asset_memory[-1] - self.asset_memory[0]

    def _trade(self, actions):
        # Simplified logic for demonstration — can be expanded to simulate buying/selling
        self.trades += 1
        self.cost += np.sum(np.abs(actions)) * self.buy_cost_pct
        
    def save_asset_memory(self):
        """
        Return account value over time for analysis.
        """
        date_list = list(self.df.date.unique())[:len(self.asset_memory)]
        df_account_value = pd.DataFrame({
            "date": date_list,
            "account_value": self.asset_memory
        })
        return df_account_value