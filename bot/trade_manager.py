# bot/trade_manager.py

from strategies.strategy import ScalpingStrategy
from config.config import TRADE_SETTINGS
from data.database import Database
import time
from bot.three_commas_api import ThreeCommasAPI

class TradeManager:
    def __init__(self):
        self.api = ThreeCommasAPI(api_key="fe64a72ea3b94652b71ed29c835e5d1243eb6e371b664321ab5214246aa36c94", api_secret="dda18228b34d2905b30a3511afa11a5a7bb80bddbf9b51f5f63d9b5383a77ebe9a207fff847fdab08f498b383f79af2ce3bdc7d0aadec31d595e2ab952c61780e5f874aae088275a1e67078d3a48b6647766696fe1bc1e70df426152466418ef6eb9f0e1")
        self.strategy = ScalpingStrategy(
            take_profit=TRADE_SETTINGS["take_profit"],
            stop_loss=TRADE_SETTINGS["stop_loss"],
            price_threshold=TRADE_SETTINGS["price_threshold"]
        )

    def run(self):
        print("Запуск бота для скальпинга через 3Commas...")
        while True:
            try:
                account_info = self.api.get_account_info()
                print("Информация об аккаунте:", account_info)

                current_price = self.api.get_price(TRADE_SETTINGS["pair"])
                print(f"Текущая цена: {current_price}")

                if self.strategy.should_buy(current_price):
                    order = self.api.place_order(TRADE_SETTINGS["pair"], "BUY", TRADE_SETTINGS["quantity"])
                    print("Ордер на покупку размещен:", order)
                    # Логирование сделки
                    Database().log_trade(
                        TRADE_SETTINGS["pair"], "BUY", TRADE_SETTINGS["quantity"], current_price
                    )

                sell_reason = self.strategy.should_sell(current_price)
                if sell_reason:
                    order = self.api.place_order(TRADE_SETTINGS["pair"], "SELL", TRADE_SETTINGS["quantity"])
                    print(f"Ордер на продажу размещен ({sell_reason}):", order)
                    # Логирование сделки
                    Database().log_trade(
                        TRADE_SETTINGS["pair"], "SELL", TRADE_SETTINGS["quantity"], current_price
                    )
                    self.strategy.entry_price = None  # Сбросить точку входа после продажи

                time.sleep(1)  # Частота обновления (1 секунда)
            except Exception as e:
                print("Ошибка:", e)
                time.sleep(5)