import numpy as np
import pandas as pd
import gym
from gym import spaces

class CryptoTradingEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    def __init__(self, df, crypto_dim=5, hmax=100, initial_amount=1e6,
                 buy_cost_pct=0.0001, sell_cost_pct=0.0001, reward_scaling=1e-4,
                 tech_indicator_list=None, featured=False, sentiment=False):
        super(CryptoTradingEnv, self).__init__()

        self.df = df.reset_index(drop=True)
        self.crypto_dim = len(self.df['tic'].unique())
        self.hmax = hmax
        self.initial_amount = initial_amount
        self.cash = initial_amount
        self.buy_cost_pct = buy_cost_pct
        self.sell_cost_pct = sell_cost_pct
        self.reward_scaling = reward_scaling
        self.featured = featured
        self.sentiment = sentiment
        self.action_space = spaces.Box(low=-1, high=1, shape=(self.crypto_dim,))
        
        #    Observation space: [ cash ] + [ stocks ] + [ prices ] ..(?) + turbulence & volatility ..(?) + sentiment
        basic_shape = 1 + 2 * self.crypto_dim
        extra_features = 0

        if self.featured:
            extra_features += 2  # turbulence + volatility
        if self.sentiment:
            extra_features += 1  # fear & greed index

        obs_shape = basic_shape + extra_features



        # self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(obs_shape,), dtype=np.float32)
        # makes training more stable because the agent knows all obs are bounded in [0,1]:
        self.observation_space = spaces.Box(low=0, high=1, shape=(obs_shape,), dtype=np.float32)


        # self.total_rewards = 0 or rewards_memory =  use for tracking cumulative reward history across episodes (e.g., for training curves)
        self.reset()
      
    def reset(self):
        self.day = 0
        self.data = self.df.loc[self.df.date == self.df.date.unique()[self.day]]
        self.terminal = False
        self.cash = self.initial_amount
        self.total_asset = self.initial_amount
        # no initial "assets at the beginning.":
        self.stocks = np.zeros(self.crypto_dim, dtype=float)
        self.asset_memory = [self.initial_amount]

        prices = self.data.close.values
        
        basic_state = [self.cash] + list(self.stocks) + prices.tolist()
        
        if self.featured:
            turbulence = 0.0
            volatility = 0.0
            basic_state = basic_state + [turbulence, volatility] 

        if self.sentiment:
            fear_greed_value = 0
            basic_state = basic_state + [fear_greed_value]

        self.state = basic_state 
        
        return np.array(self.state, dtype=np.float32)

    # fixed: min and max don't match up with any account value: resolved, fresh download data if start date changes

    def step(self, actions):

        prices = self.data.close.values

        # --- Dynamic hmax per asset ---
        # Max units we could buy for each asset with available cash (scaled by self.hmax)
        dynamic_hmax = np.floor((self.cash / (prices * (1 + self.buy_cost_pct))) * (self.hmax / 100))
        # Apply dynamic limit to actions
        actions = np.clip(actions, -1, 1) * dynamic_hmax
        # ---------------------------------------------------

        # SELL
        for i in np.where(actions < 0)[0]:
            sell_amount = min(self.stocks[i], -actions[i])
            if sell_amount > 1e-8:  # Avoid floating-point noise trades
                self.stocks[i] -= sell_amount
                self.cash += prices[i] * sell_amount * (1 - self.sell_cost_pct)

        # BUY
        for i in np.where(actions > 0)[0]:
            max_buy = self.cash // (prices[i] * (1 + self.buy_cost_pct))
            buy_amount = min(max_buy, actions[i])
            if buy_amount > 1e-8:  # Avoid floating-point noise trades
                self.stocks[i] += buy_amount
                self.cash -= prices[i] * buy_amount * (1 + self.buy_cost_pct)

        # Advance to next day or mark terminal
        self.day += 1
        if self.day < len(self.df.date.unique()):
            self.data = self.df.loc[self.df.date == self.df.date.unique()[self.day]]
        else:
            self.terminal = True

        # Calculate total assets & reward
        prices = self.data.close.values
        # "reflects cash + holdings (mark-to-market value) after each trade":
        self.total_asset = self.cash + np.sum(self.stocks * prices)
        reward = (self.total_asset - self.asset_memory[-1]) * self.reward_scaling
        # NOTE is used? :
        self.asset_memory.append(self.total_asset)

          # --- Base state ---
        basic_state = [self.cash] + list(self.stocks) + prices.tolist()

        # NOTE : consider extra precausion if flags are set by mistake but no data / column is provided then 0 value bug could be undetected
            # --- Extra features if enabled ---
        if self.featured:
            turbulence = self.data["turbulence"].iloc[0] if "turbulence" in self.data else 0
            volatility = self.data["volatility"].iloc[0] if "volatility" in self.data else 0
            basic_state += [turbulence, volatility]
        
        if self.sentiment:
            fear_greed_value = self.data["fear_greed_norm"].iloc[0] if "fear_greed_norm" in self.data else 0
            basic_state += [fear_greed_value]

        self.state = basic_state

 
        return np.array(self.state), reward, self.terminal, {}


                    # TODO add later: (& update observation space)
                    # sum([self.data[tech].values.tolist() for tech in self.tech_indicator_list], [])


        #   "window": i + 1,  "initial_acc_val": account_values.iloc[0],  "min_account_value": account_values.min(),  "max_account_value": account_values.max(), "final_acc_val": account_values.iloc[-1],

    # def _get_total_asset(self):
    #     prices = self.data.close.values
    #     return self.cash + np.sum(self.stocks * prices)

    # ** Executes trades based on action values - Positive action: Buy -  Negative action: Sell updating the account value on each step
    # Assumes self.state = [cash, holdings..., prices..., indicators...]
    # Prevents buying more than available cash allows.
    # Updates both cash (self.state[0]) and holdings (self.state[1:1+self.crypto_dim]).
    # Accumulates trading cost and trades count.
    def _trade(self, actions):
        prices = self.data.close.values
        actions = actions.astype(float)

        # Scale actions to max trade size (hmax)
        scaled_actions = actions * self.hmax

        for i in range(self.crypto_dim):
            action = scaled_actions[i]
            price = prices[i]

            # SELL
            if action < 0:
                sell_amount = min(abs(action), self.stocks[i])
                self.cash += sell_amount * price * (1 - self.sell_cost_pct)
                self.stocks[i] -= sell_amount

            # BUY
            elif action > 0:
                max_buyable = self.cash // (price * (1 + self.buy_cost_pct))
                buy_amount = min(action, max_buyable)
                self.cash -= buy_amount * price * (1 + self.buy_cost_pct)
                self.stocks[i] += buy_amount

        # Optional: track trade cost for logging
        self.trades += 1
        self.cost += np.sum(np.abs(actions)) * self.buy_cost_pct