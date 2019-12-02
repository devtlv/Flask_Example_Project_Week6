import requests


def get_stock_exchanges():
    stock_exchanges_response = requests.get('https://api.worldtradingdata.com/api/v1/exchange_list',
                                            {
                                                'api_token': 'CfKzuYYPqeekR95Ud2Hime7E8cMxz6FgspmUWwbDQiavYJ0Tk55fEHAHpHeN'
                                            })
    stock_exchanges_response.raise_for_status()
    stock_exchanges = stock_exchanges_response.json()
    if 'message' in stock_exchanges:
        raise ValueError(stock_exchanges['message'])
    return stock_exchanges
