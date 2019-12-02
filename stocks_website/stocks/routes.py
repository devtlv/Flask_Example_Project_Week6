import requests
from flask import Blueprint, render_template

from stocks_website.exchanges import get_stock_exchanges

stocks_routes = Blueprint('stocks', __name__, template_folder='templates/')


@stocks_routes.route('/exchanges/<exchange>')
def exchanges(exchange):
    stock_exchanges = get_stock_exchanges()

    search_response = requests.get('https://api.worldtradingdata.com/api/v1/stock_search',
                                   {
                                       'api_token': 'CfKzuYYPqeekR95Ud2Hime7E8cMxz6FgspmUWwbDQiavYJ0Tk55fEHAHpHeN',
                                       'stock_exchange': exchange
                                   })
    search_response.raise_for_status()
    search_data = search_response.json()
    if 'message' in search_data and 'data' not in search_data:
        raise ValueError(search_data['message'])
    print(search_data)
    return render_template('exchanges.html',
                           stock_exchanges=stock_exchanges,
                           search_data=search_data['data'])


