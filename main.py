import requests
import os
import argparse
from dotenv import load_dotenv


def get_currency_value(api_key, base_currency, target_currency, amount):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}/{amount}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as error:
        print(f"HTTPError: {error}")
        return None
    return response.json()["conversion_result"]


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    parser = argparse.ArgumentParser(description="Программа для конвертирования валют")
    parser.add_argument(
        "-b", "--base_currency", help="Базовая валюта (по умолчанию RUB)", default="RUB"
    )
    parser.add_argument(
        "-t", "--target_rate", help="Целевая валюта (по умолчанию USD)", default="USD"
    )
    parser.add_argument(
        "-m", "--money", type=float, help="Сумма денег (по умолчанию 1000)", default=1000
    )
    args = parser.parse_args()

    base_currency = args.base_currency
    target_rate = args.target_rate
    money = args.money

    conversion_result = get_currency_value(api_key, base_currency, target_rate, money)
    if conversion_result:
        print(f"Конвертировання сумма: {conversion_result} {target_rate}")


if __name__ == "__main__":
    main()
