import json
import logging

logging.basicConfig(level=logging.INFO)

def analyze_cashback(transactions, year, month):
    """Анализирует категории с повышенным кешбэком."""
    logging.info(f"Анализ кешбэка за {year}-{month}")

    filtered = [t for t in transactions if t["Дата операции"].year == year and t["Дата операции"].month == month]
    categories = {}

    for t in filtered:
        category = t["Категория"]
        cashback = t.get("Кешбэк", 0)
        categories[category] = categories.get(category, 0) + cashback

    top_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)[:3]

    return json.dumps({"top_cashback_categories": top_categories}, ensure_ascii=False, indent=4)
