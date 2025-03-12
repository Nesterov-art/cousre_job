import json
import logging
from datetime import datetime
from collections import defaultdict

logging.basicConfig(filename="services.log", level=logging.INFO)

def analyze_cashback(data, year, month):
    cashback = defaultdict(int)

    for transaction in data:
        trans_date = datetime.strptime(transaction["Дата операции"], "%Y-%m-%d")
        if trans_date.year == year and trans_date.month == month:
            category = transaction["Категория"]
            amount = float(transaction["Сумма операции"])
            if amount < 0:
                cashback[category] += abs(amount) * 0.01

    return json.dumps(cashback, ensure_ascii=False, indent=4)

def simple_search(data, query):
    results = [t for t in data if query.lower() in t["Категория"].lower() or query.lower() in t["Описание"].lower()]
    return json.dumps(results, ensure_ascii=False, indent=4)
