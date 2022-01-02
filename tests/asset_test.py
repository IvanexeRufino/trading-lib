from domain_classes.asset import Asset
from unittest import TestCase

from tests.mocks.asset_mock_provider import MockAssetProvider


class TestAsset(TestCase):
    def test_asset_loads_candles_info(self):
        mock_provider = MockAssetProvider()
        asset: Asset = mock_provider.get_asset_info("ADAUSDT")

        self.assertTrue(asset.price_history[3].is_positive())
