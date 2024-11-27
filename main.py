# main.py

from binance.client import Client

API_KEY = "1df47f64439642dc50816c3af891cb0eec130766852bf3075649168746b64cce"
API_SECRET = "b23353d0896e1b9366467b0730faedd0c6ea7f06f1598e9e49aff72fafcbfee2"
TESTNET_URL = 'https://testnet.binancefuture.com'

# Инициализация клиента
client = Client(API_KEY, API_SECRET, testnet=True)
client.API_URL = TESTNET_URL

try:
    # Получение баланса
    balances = client.futures_account_balance()
    print("Баланс аккаунта:")
    for asset in balances:
        print(f"{asset['asset']}: {asset['balance']}")
except Exception as e:
    print("Ошибка:", e)