import json
import datetime
import logging
from utils import load_user_settings, get_exchange_rates, get_stock_prices
import pandas as pd

logging.basicConfig(level=logging.INFO)


def get_home_data(date_str):
    """Формирует JSON-ответ для главной страницы."""
    logging.info("Формируем данные для главной страницы")

    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

    settings = load_user_settings()

    exchange_rates = get_exchange_rates(settings["exchange_rates"])
    stock_prices = get_stock_prices(settings["user_stocks"])

    df = pd.read_excel("data/operations.xlsx")
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], format="%d.%m.%Y %H:%M:%S", dayfirst=True)
    df_filtered = df[(df["Дата операции"] >= date.replace(day=1)) & (df["Дата операции"] <= date)]

    result = {
        "date": date_str,
        "exchange_rates": exchange_rates,
        "stock_prices": stock_prices,
        "top_transactions": df_filtered.nlargest(5, "Сумма").to_dict(orient="records"),
    }

    return json.dumps(result, ensure_ascii=False, indent=4)
