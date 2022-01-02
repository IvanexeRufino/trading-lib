class Candle:
    def __init__(
        self,
        open_time: int,
        open_price: float,
        close_price: float,
        high_price: float,
        low_price: float,
    ):
        self.open_time = open_time
        self.open = open_price
        self.high = high_price
        self.low = low_price
        self.close = close_price

    def is_positive(self):
        return self.close >= self.open
