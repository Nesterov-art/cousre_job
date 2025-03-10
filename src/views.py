from datetime import datetime
import logging
import requests
import pandas as pd
import http.client
from src.utils import parse_date, calculate_cashback, filter_data_by_date


def get_greeting():
    now = datetime.now()
    if 5 <= now.hour < 12:
        return "Доброе утро"
    elif 12 <= now.hour < 18:
        return "Добрый день"
    elif 18 <= now.hour < 22:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def get_currency_rates():
    api_key = "x6saMiG4BaQDrtcnM7f2aMiJbnwTfHVz"
    url = f"http://api.currencylayer.com/live?access_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            return data["quotes"]
        else:
            logging.error("Ошибка при получении данных от API.")
            return {}
    else:
        logging.error(f"Ошибка HTTP: {response.status_code}")
        return {}


def get_stock_prices():
    api_key = "76a6c9450c8bca48c2476cfd40fe1d87"
    conn = http.client.HTTPSConnection("api.marketstack.com")
    conn.request("GET", "/v1/eod?access_key={76a6c9450c8bca48c2476cfd40fe1d87}&symbols=AAPL")
    res = conn.getresponse()
    data = res.read()
    response = requests.get(url=api_key)

    if response.status_code == 200:
        data = response.json()
        return {stock: data[stock]['quote']['latestPrice'] for stock in data}
    else:
        logging.error(f"Ошибка HTTP: {response.status_code}")
        return {}


def get_home_data(date_str):
    date = parse_date(date_str)
    start_date = date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    data = pd.read_excel('data/operations.xlsx')
    filtered_data = filter_data_by_date(data, start_date, date)

    greeting = get_greeting()
    cards = filtered_data['card'].unique()
    result = {
        "greeting": greeting,
        "cards": [],
        "currency_rates": get_currency_rates(),
        "stock_prices": get_stock_prices()
    }

    for card in cards:
        card_data = filtered_data[filtered_data['card'] == card]
        total_spent = card_data['amount'].sum()
        cashback = calculate_cashback(total_spent)
        top_transactions = card_data.nlargest(5, 'amount').to_dict('records')
        result["cards"].append({
            "last_four_digits": str(card)[-4:],
            "total_spent": total_spent,
            "cashback": cashback,
            "top_transactions": top_transactions
        })

    return result