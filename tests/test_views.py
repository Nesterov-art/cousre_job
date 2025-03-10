import unittest
from unittest.mock import patch
from src.views import get_greeting, get_home_data, get_currency_rates

class TestViews(unittest.TestCase):
    def test_get_greeting(self):
        self.assertIn(get_greeting(), ["Доброе утро", "Добрый день", "Добрый вечер", "Доброй ночи"])

    @patch('requests.get')
    def test_get_currency_rates(self, mock_get):
        mock_response = {
            "quotes": {
                "USDAUD": 1.278342,
                "USDEUR": 1.278342,
                "USDGBP": 0.908019,
                "USDPLN": 3.731504
            },
            "source": "USD",
            "success": True,
            "timestamp": 1432400348
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = get_currency_rates()
        self.assertEqual(result, mock_response["quotes"])

if __name__ == "__main__":
    unittest.main()