from binance.client import Client
from configparser import ConfigParser
from domain_classes.asset import Asset
from domain_classes.candle import Candle


class CryptoBinanceProvider:
    def __init__(self):
        config = ConfigParser()
        config.read("config.ini")
        api_key = config["binance"]["API_KEY"]
        secret_key = config["binance"]["API_SECRET"]

        self.client = Client(api_key, secret_key)

    def get_candle_from_binance_kline(self, kline):
        return Candle(
            open_time=int(kline[0]),
            open_price=float(kline[1]),
            close_price=float(kline[4]),
            high_price=float(kline[2]),
            low_price=float(kline[3]),
        )

    def get_asset_info(
        self, symbol: str, interval: str, start_point: str, end_point: str
    ) -> Asset:
        klines = self.client.get_historical_klines(
            symbol, interval, start_point, end_point
        )

        candles: list[Candle] = []

        for kline in klines:
            candles.append(self.get_candle_from_binance_kline(kline))

        return Asset(symbol=symbol, price_history=candles)
