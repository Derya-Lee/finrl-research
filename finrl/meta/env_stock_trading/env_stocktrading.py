import numpy as np
import pandas as pd
import gym
from gym import spaces

class StockTradingEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    #TODO remove default value stock_dim=30,
    def __init__(self, df, stock_dim=30, hmax=100, initial_amount=1e6,
                 buy_cost_pct=0.0001, sell_cost_pct=0.0001, reward_scaling=1e-4,
                 tech_indicator_list=None):
        super(StockTradingEnv, self).__init__()

        self.df = df.reset_index(drop=True)
        self.stock_dim = len(self.df['tic'].unique())
        self.hmax = hmax
        self.initial_amount = initial_amount
        self.buy_cost_pct = buy_cost_pct
        self.sell_cost_pct = sell_cost_pct
        self.reward_scaling = reward_scaling
        self.tech_indicator_list = tech_indicator_list if tech_indicator_list else ['macd', 'rsi_30', 'cci_30']
        self.action_space = spaces.Box(low=-1, high=1, shape=(self.stock_dim,))
        obs_shape = 1 + 2 * self.stock_dim + len(self.tech_indicator_list) * self.stock_dim
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(obs_shape,), dtype=np.float32)
        # self.observation_space = spaces.Box(
        #     low=-np.inf, high=np.inf, shape=(1 + 2 * self.stock_dim + len(self.tech_indicator_list) * self.stock_dim,)
        # )

        self.reset()

    def reset(self):
        self.day = 0
        self.data = self.df.loc[self.df.date == self.df.date.unique()[self.day]]
        self.terminal = False
        self.state = [self.initial_amount] + \
             [0] * self.stock_dim + \
             self.data.close.values.tolist() + \
             sum([self.data[tech].values.tolist() for tech in self.tech_indicator_list], [])
        # Debug check:
        # print("State length:", len(self.state))
        # print("Observation space:", self.observation_space.shape)

        self.asset_memory = [self.initial_amount]
        self.cost = 0
        self.trades = 0
        return np.array(self.state)

    def step(self, actions):
        self.terminal = self.day >= len(self.df.date.unique()) - 1
        if self.terminal:
            return self.state, self._reward(), self.terminal, {}

        actions = actions * self.hmax
        begin_total_asset = self._get_total_asset()

        self._trade(actions)

        self.day += 1
        self.data = self.df.loc[self.df.date == self.df.date.unique()[self.day]]
        self.state = [self._get_total_asset()] + \
                     [0] * self.stock_dim + \
                     self.data.close.values.tolist() + \
                     sum([self.data[tech].values.tolist() for tech in self.tech_indicator_list], [])

        end_total_asset = self._get_total_asset()
        reward = (end_total_asset - begin_total_asset) * self.reward_scaling
        self.asset_memory.append(end_total_asset)

        return np.array(self.state), reward, self.terminal, {}

    def _get_total_asset(self):
        return self.state[0]  # simply return current balance (can be expanded)

    def _reward(self):
        return self.asset_memory[-1] - self.asset_memory[0]

    def _trade(self, actions):
        # Simplified logic for demonstration — can be expanded to simulate buying/selling
        self.trades += 1
        self.cost += np.sum(np.abs(actions)) * self.buy_cost_pct
