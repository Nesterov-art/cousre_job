import os
import json
import requests
import pandas as pd
from dotenv import load_dotenv


load_dotenv()

# Загружаем настройки пользователя
def load_user_settings():
    path = r"C:\Users\GAYniy\PycharmProjects\cousre_job\user_settings.json"  # Абсолютный путь
    with open(path, "r", encoding="utf-8") as f:
        settings = json.load(f)
    return settings


# Получение курсов валют
def get_exchange_rates():
    api_key = os.getenv("CURRENCY_API_KEY")
    url = f"https://api.apilayer.com/currency_data/live?access_key={api_key}&currencies=USD,EUR,RUB"
    response = requests.get(url).json()
    return response.get("quotes", {})


# Получение цен на акции
def get_stock_prices(symbols):
    api_key = os.getenv("STOCKS_API_KEY")
    prices = {}

    for symbol in symbols:
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{symbol}"
        response = requests.get(url).json()
        prices[symbol] = response.get("conversion_rates", {}).get("USD", "N/A")

    return prices
