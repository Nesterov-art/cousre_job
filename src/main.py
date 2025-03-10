from src.views import get_home_data
from src.services import analyze_cashback_categories, simple_search, search_by_phone
from src.reports import spending_by_category
import pandas as pd

def main():
    data = pd.read_excel('data/operations.xlsx')
    print(get_home_data("2023-10-20 12:00:00"))
    print(analyze_cashback_categories(data, 2025, 3))
    print(simple_search(data, "Coffee"))
    print(search_by_phone(data))
    print(spending_by_category(data, "Food"))

if __name__ == "__main__":
    main()