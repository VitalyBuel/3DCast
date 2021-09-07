import requests
import json
from config import keys, API_KEY

class ConvertionException(Exception):
    pass

class APIException:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно проверить одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(
            f'http://api.exchangeratesapi.io/v1/latest'
            f'?access_key={API_KEY}'
            f'&base={quote_ticker}'
            f'&symbols={base_ticker}'
        )
        total_base = json.loads(r.content)['rates'][base_ticker]

        return  total_base
