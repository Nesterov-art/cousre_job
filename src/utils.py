import logging
import json

logging.basicConfig(level=logging.INFO)


def load_user_settings():
    """Загружает настройки пользователя из JSON."""
    logging.info("Загружаем настройки пользователя")

    try:
        with open("user_settings.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("Файл user_settings.json не найден")
        return {}
