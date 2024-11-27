# data/database.py

import sqlite3

class Database:
    def __init__(self, db_name="trading_bot.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS trades (
                    id INTEGER PRIMARY KEY,
                    pair TEXT,
                    side TEXT,
                    quantity REAL,
                    price REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def log_trade(self, pair, side, quantity, price):
        with self.connection:
            self.connection.execute("""
                INSERT INTO trades (pair, side, quantity, price)
                VALUES (?, ?, ?, ?)
            """, (pair, side, quantity, price))