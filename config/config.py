# config/config.py

API_KEY = "1df47f64439642dc50816c3af891cb0eec130766852bf3075649168746b64cce"
API_SECRET = "b23353d0896e1b9366467b0730faedd0c6ea7f06f1598e9e49aff72fafcbfee2"

# Использовать тестовую сеть Binance
TESTNET = True

# Настройки торговой стратегии
TRADE_SETTINGS = {
    "pair": "BTCUSDT",
    "interval": "1m",
    "quantity": 0.001,
    "take_profit": 1.005,
    "stop_loss": 0.995,
    "price_threshold": 65000
}