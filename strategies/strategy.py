# strategies/strategy.py

class ScalpingStrategy:
    def __init__(self, take_profit, stop_loss, price_threshold):
        self.take_profit = take_profit
        self.stop_loss = stop_loss
        self.price_threshold = price_threshold
        self.entry_price = None

    def should_buy(self, current_price):
        """Покупка при падении цены ниже порога."""
        if self.entry_price is None and current_price <= self.price_threshold:
            self.entry_price = current_price
            return True
        return False

    def should_sell(self, current_price):
        """Продажа при достижении take_profit или stop_loss."""
        if self.entry_price:
            if current_price >= self.entry_price * self.take_profit:
                return "take_profit"
            elif current_price <= self.entry_price * self.stop_loss:
                return "stop_loss"
        return None