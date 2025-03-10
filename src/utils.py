from datetime import datetime
import logging

# Настройка логирования
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )

def parse_date(date_str, date_format="%Y-%m-%d %H:%M:%S"):
    """Функция для преобразования строки в дату"""
    try:
        return datetime.strptime(date_str, date_format)
    except ValueError as e:
        logging.error(f"Ошибка при преобразовании даты: {e}")
        raise


def calculate_cashback(amount):
    """Функция для вычисления кешбэка"""
    return int(amount // 100)


def filter_data_by_date(data, start_date, end_date):
    """Функция для фильтрации данных по дате"""
    return data[(data['date'] >= start_date) & (data['date'] <= end_date)]