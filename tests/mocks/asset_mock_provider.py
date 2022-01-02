from domain_classes.candle import Candle
from domain_classes.asset import Asset


class MockAssetProvider:
    def get_asset_info(
        self,
        symbol: str,
        interval: str = None,
        start_point: str = None,
        end_point: str = None,
    ) -> Asset:
        return Asset(
            symbol,
            [
                Candle(0, 50, 100, 150, 60),
                Candle(1, 100, 125, 150, 60),
                Candle(2, 125, 60, 150, 60),
                Candle(3, 60, 150, 150, 60),
            ],
        )
