from candle import Candle
from datetime import datetime
from pandas import DataFrame
from binance.client import Client


class Asset:

    symbol: str
    price_history: list[Candle]

    def __init__(self, symbol: str, price_history: list[Candle]):
        self.symbol = symbol
        self.price_history = price_history
