import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


def spending_by_category(df, category, start_date):
    """Анализирует траты по категории за 3 месяца."""
    logging.info(f"Анализируем траты в категории {category} с {start_date}")

    start_date = pd.to_datetime(start_date)
    three_months_ago = start_date - pd.DateOffset(months=3)

    filtered_df = df[(df["Категория"] == category) & (df["Дата операции"] >= three_months_ago)]

    return filtered_df  # Теперь возвращаем DataFrame
