import pytest
import json
from src.utils import load_user_settings

def test_load_user_settings(mocker):
    mocker.patch("builtins.open", mocker.mock_open(read_data='{"exchange_rates": ["USD", "EUR"], "user_stocks": ["AAPL"]}'))
    settings = load_user_settings()
    assert "exchange_rates" in settings
    assert settings["exchange_rates"] == ["USD", "EUR"]
