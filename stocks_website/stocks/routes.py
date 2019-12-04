import requests
from flask import Blueprint, render_template, current_app as app

stocks_routes = Blueprint('stocks', __name__, template_folder='templates')


@stocks_routes.route('/exchanges/<exchange>')
def exchanges(exchange):
    search_response = requests.get('https://api.worldtradingdata.com/api/v1/stock_search',
                                   {
                                       'api_token': app.config.world_trading_data_api_token,
                                       'stock_exchange': exchange
                                   })
    search_response.raise_for_status()
    search_data = search_response.json()
    if 'message' in search_data and 'data' not in search_data:
        raise ValueError(search_data['message'])
    print(search_data)
    return render_template('stocks/exchanges.html',
                           stock_exchanges=app.config.stock_exchanges,
                           search_data=search_data['data'])


