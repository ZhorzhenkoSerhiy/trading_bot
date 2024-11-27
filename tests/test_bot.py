# tests/test_bot.py

import unittest
from bot.binance_api import BinanceAPI
from strategies.strategy import ScalpingStrategy

class TestBot(unittest.TestCase):
    def test_get_price(self):
        api = BinanceAPI()
        price = api.get_price("BTCUSDT")
        self.assertGreater(price, 0)

    def test_strategy_buy(self):
        strategy = ScalpingStrategy(take_profit=1.02, stop_loss=0.98)
        self.assertTrue(strategy.should_buy(50000))

if __name__ == "__main__":
    unittest.main()