import logging
import json
import os
import requests
logging.basicConfig(level=logging.INFO)


def load_user_settings():
    """Загружает настройки пользователя из JSON."""
    logging.info("Загружаем настройки пользователя")

    try:
        with open("user_settings.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("Файл user_settings.json не найден")
        return {}


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