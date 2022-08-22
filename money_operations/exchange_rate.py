import requests

def get_exchange_rate(currency_from: str, currency_to: str) -> float:
    url = f'https://api.exchangerate.host/convert?from={currency_from}&to={currency_to}'
    response = requests.get(url)
    data = response.json()

    return float(data["result"])
