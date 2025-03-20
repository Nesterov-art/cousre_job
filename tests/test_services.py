import pytest
import json
from src.services import analyze_cashback

@pytest.fixture
def transactions():
    return [
        {"Дата операции": "2023-12-10", "Категория": "Продукты", "Кешбэк": 100},
        {"Дата операции": "2023-12-15", "Категория": "Фастфуд", "Кешбэк": 200},
        {"Дата операции": "2023-12-20", "Категория": "Фастфуд", "Кешбэк": 150},
    ]

def test_analyze_cashback(transactions):
    result = json.loads(analyze_cashback(transactions, 2023, 12))
    assert "top_cashback_categories" in result
    assert len(result["top_cashback_categories"]) > 0
    assert result["top_cashback_categories"][0][0] == "Фастфуд"
