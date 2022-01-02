from domain_classes.candle import Candle


class Asset:

    symbol: str
    price_history: list[Candle]

    def __init__(self, symbol: str, price_history: list[Candle]):
        self.symbol = symbol
        self.price_history = price_history
