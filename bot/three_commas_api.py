import requests

class ThreeCommasAPI:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.3commas.io/public/api"

    def get_account_info(self):
        """Получить информацию об аккаунте."""
        endpoint = f"{self.base_url}/ver1/accounts"
        headers = {"APIKEY": self.api_key, "SECRET": self.api_secret}
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Ошибка API: {response.text}")

    def place_order(self, pair, side, quantity, price=None):
        """Разместить ордер на 3Commas."""
        endpoint = f"{self.base_url}/ver1/smart_trades/create_simple_trade"
        headers = {"APIKEY": self.api_key, "SECRET": self.api_secret}
        payload = {
            "pair": pair,
            "type": "market" if not price else "limit",
            "quantity": quantity,
            "side": side.lower(),  # buy или sell
            "price": price,
        }
        response = requests.post(endpoint, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Ошибка API: {response.text}")