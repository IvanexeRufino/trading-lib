from domain_classes.asset import Asset
from unittest import TestCase
from providers.crypto_binance_provider import CryptoBinanceProvider
from binance.client import Client


class TestBinanceProvider(TestCase):
    def test_binance_provider_gets_data(self):
        provider = CryptoBinanceProvider()
        asset: Asset = provider.get_asset_info(
            "ADAUSDT", Client.KLINE_INTERVAL_1HOUR, "2021-01-01", "2021-01-02"
        )

        self.assertEquals(0.18051, asset.price_history[0].close)
        self.assertEquals(0.18146, asset.price_history[0].high)
        self.assertEquals(0.17831, asset.price_history[0].low)
        self.assertEquals(0.18134, asset.price_history[0].open)
        self.assertFalse(asset.price_history[0].is_positive())
        self.assertEquals(25, len(asset.price_history))
