import requests
import os
import argparse
from dotenv import load_dotenv


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


def get_currencyvalue(base_currency):
    try:
        response = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}")
        response.raise_for_status()
    except requests.HTTPError as error:
        print("HTTPError")
        return None
    return response.json()


def convert_amount(base_currency, target_rate, money):
    response = get_currencyvl(base_currency)
    if response is None:
        return None, None
    target_rate_value = response["conversion_rates"][target_rate]
    converted = money * target_rate_value
    return converted, target_rate_value


def main():
    base_currency = args.base_currency
    target_rate = args.target_rate
    money = args.money

    converted, target_rate_value = convert_amount(base_currency, target_rate, money)
    if converted is None:
        return
    print(f"Курс {base_currency} к {target_rate}: {target_rate_value}")
    print(f"Конвертированная сумма: {converted} {target_rate}")


if __name__ == "__main__":
    main()
