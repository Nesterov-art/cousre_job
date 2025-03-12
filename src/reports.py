import json
import pandas as pd
from datetime import datetime
from functools import wraps


def save_report(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            file_name = filename or f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
            return result

        return wrapper

    return decorator


@save_report()
def spending_by_category(df, category, date=None):
    if date is None:
        date = datetime.now()
    else:
        date = datetime.strptime(date, "%Y-%m-%d")

    start_date = date - pd.DateOffset(months=3)
    df["Дата операции"] = pd.to_datetime(df["Дата операции"])

    filtered_df = df[(df["Дата операции"] >= start_date) &
                     (df["Дата операции"] <= date) &
                     (df["Категория"] == category) &
                     (df["Сумма операции"] < 0)]

    return filtered_df.to_dict(orient="records")
