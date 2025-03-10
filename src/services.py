import pandas as pd
import logging

from src.utils import filter_data_by_date


def analyze_cashback_categories(data, year, month):
    start_date = datetime(year, month, 1)
    end_date = datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1)
    filtered_data = filter_data_by_date(data, start_date, end_date)
    cashback_by_category = filtered_data.groupby('category')['amount'].sum() // 100
    return cashback_by_category.to_dict()

def simple_search(data, search_term):
    return data[data.apply(lambda row: search_term in row['description'] or search_term in row['category'], axis=1)].to_dict('records')

def search_by_phone(data):
    import re
    phone_pattern = re.compile(r'\+7\s?\d{3}\s?\d{3}-\d{2}-\d{2}')
    return data[data['description'].apply(lambda x: bool(phone_pattern.search(x)))].to_dict('records')