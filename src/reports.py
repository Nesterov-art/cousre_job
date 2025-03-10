import pandas as pd
import logging
from functools import wraps


def report_decorator(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            output_filename = filename if filename else f"{func.__name__}_report.json"
            pd.DataFrame(result).to_json(output_filename, orient='records')
            logging.info(f"Report saved to {output_filename}")
            return result
        return wrapper
    return decorator

@report_decorator()
def spending_by_category(data, category, date=None):
    if date is None:
        date = pd.Timestamp.now()
    start_date = date - pd.DateOffset(months=3)
    filtered_data = data[(data['date'] >= start_date) & (data['date'] <= date) & (data['category'] == category)]
    return filtered_data.to_dict('records')