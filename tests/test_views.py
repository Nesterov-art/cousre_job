import pytest
import json
from src.views import get_home_data

def test_get_home_data(mocker):
    mocker.patch("src.utils.get_exchange_rates", return_value={"USD": 75.5, "EUR": 82.3})
    mocker.patch("src.utils.get_stock_prices", return_value={"AAPL": 150.2})

    result = json.loads(get_home_data("2023-12-31 12:00:00"))
    assert "exchange_rates" in result
    assert "stock_prices" in result
    assert result["exchange_rates"]["USD"] == 75.5
    assert result["stock_prices"]["AAPL"] == 150.2
