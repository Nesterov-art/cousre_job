import json
import datetime
from src.utils import get_exchange_rates, get_stock_prices, load_user_settings


def get_home_data(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    hour = date_obj.hour

    if 5 <= hour < 12:
        greeting = "Доброе утро"
    elif 12 <= hour < 18:
        greeting = "Добрый день"
    elif 18 <= hour < 23:
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"

    settings = load_user_settings()

    exchange_rates = get_exchange_rates()
    stock_prices = get_stock_prices(settings["user_stocks"])

    response = {
        "greeting": greeting,
        "exchange_rates": exchange_rates,
        "stock_prices": stock_prices
    }

    return json.dumps(response, ensure_ascii=False, indent=4)
