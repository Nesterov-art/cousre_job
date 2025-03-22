import os
import pandas as pd
from src.views import get_home_data
from src.reports import spending_by_category
from src.utils import load_user_settings
from src.services import analyze_cashback, simple_search



if __name__ == "__main__":
    # формируем корректный путь до файла с данными
    current_dir = os.path.dirname(__file__)
    operations_file_path = os.path.join(current_dir, '..', 'data', 'operations.xlsx')

    df = pd.read_excel(operations_file_path)
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], format="%d.%m.%Y %H:%M:%S", dayfirst=True)

    # Вызов главной страницы
    print(get_home_data("2025-03-12 14:30:00"))

    # Вызов сервисв
    # Сервисы по ТЗ должны работать со списком словарей. Сначала сделаем из датафрейма - список словарей
    operations_as_dicts = df.to_dict(orient='records')
    print(analyze_cashback(operations_as_dicts, 2021, 12))
    print(simple_search(operations_as_dicts, 'перевод'))

    # Генерация отчета
    report = spending_by_category(df, "Фастфуд", "2021-03-12")
    print(report)