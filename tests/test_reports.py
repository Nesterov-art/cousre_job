import pytest
import pandas as pd
from src.reports import spending_by_category

@pytest.fixture
def sample_dataframe():
    data = {
        "Дата операции": pd.to_datetime(["2023-01-10", "2023-02-15", "2023-03-20"]),
        "Категория": ["Продукты", "Фастфуд", "Фастфуд"],
        "Сумма": [1500, 500, 800]
    }
    return pd.DataFrame(data)

def test_spending_by_category(sample_dataframe):
    result = spending_by_category(sample_dataframe, "Фастфуд", "2023-03-20")
    assert not result.empty
    assert len(result) == 2
    assert result["Категория"].unique()[0] == "Фастфуд"
