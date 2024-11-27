from binance.client import Client
from config.config import API_KEY, API_SECRET
from config.config import TRADE_SETTINGS
from binance.client import Client
from config.config import API_KEY, API_SECRET, TESTNET

class BinanceAPI:
    def __init__(self):
        if TESTNET:
            self.client = Client(API_KEY, API_SECRET, testnet=True)
            self.client.API_URL = 'https://testnet.binance.vision/api'
        else:
            self.client = Client(API_KEY, API_SECRET)

    def get_price(self, pair):
        """Получить текущую цену пары."""
        return float(self.client.get_symbol_ticker(symbol=pair)["price"])

    def place_order(self, pair, side, quantity):
        """Открыть ордер (покупка или продажа)."""
        order = self.client.order_market(symbol=pair, side=side, quantity=quantity)
        return order