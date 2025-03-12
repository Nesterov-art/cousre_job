import pandas as pd
from src.views import get_home_data
from src.reports import spending_by_category
from src.utils import load_user_settings


if __name__ == "__main__":
    df = pd.read_excel(r"C:\Users\GAYniy\PycharmProjects\cousre_job\data\operations.xlsx")
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], format="%d.%m.%Y %H:%M:%S", dayfirst=True)

    # Вызов главной страницы
    print(get_home_data("2025-03-12 14:30:00"))


    # Генерация отчета
    report = spending_by_category(df, "Продукты", "2025-03-12")
    print(report)
