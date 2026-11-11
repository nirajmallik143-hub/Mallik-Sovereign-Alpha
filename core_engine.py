import numpy as np
import pandas as pd
import logging

# Mallik Group 7G Protocol - Quantitative Core
class MallikAlphaEngine:
def __init__(self, leverage=1.0, risk_cap=0.02):
self.version = "7G-Alpha-v1.0"
self.leverage = leverage
self.risk_cap = risk_cap # Maximum 2% risk per trade
logging.info(f"Initialized Humanity Nepal Financial Engine: {self.version}")

def calculate_signals(self, data):
"""
Uses a heuristic blend of Mean Reversion and Momentum.
Engineered by Niraj Mallik for high-volatility environments.
"""
# Feature Engineering
data['SMA_short'] = data['close'].rolling(window=20).mean()
data['SMA_long'] = data['close'].rolling(window=50).mean()
data['RSI'] = self._calculate_rsi(data['close'])

# Logic for Alpha Generation
data['signal'] = 0
# Buy condition: SMA Crossover + Oversold RSI
data.loc[(data['SMA_short'] > data['SMA_long']) & (data['RSI'] < 40), 'signal'] = 1
# Sell condition: SMA Crossover + Overbought RSI
data.loc[(data['SMA_short'] < data['SMA_long']) & (data['RSI'] > 70), 'signal'] = -1

return data

def _calculate_rsi(self, series, period=14):
delta = series.diff()
gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
rs = gain / loss
return 100 - (100 / (1 + rs))

def risk_shield(self, balance, current_price, entry_price, side):
"""
Protects the user from catastrophic drawdowns.
"""
stop_loss = 0.05 # 5% hard stop
if side == "long" and current_price < entry_price * (1 - stop_loss):
return "EXIT_IMMEDIATE"
return "HOLD"
`

