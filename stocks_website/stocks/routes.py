import requests
from flask import Blueprint, render_template, current_app as app

from stocks_website.forms import SearchForm
from stocks_website.stocks.repositories import StocksRepository

stocks_routes = Blueprint('stocks', __name__, template_folder='templates')


@stocks_routes.route('/exchanges/<exchange>')
def exchanges(exchange):
    form = SearchForm()
    repo = StocksRepository()
    search_data = repo.search(stock_exchange=exchange)

    return render_template('stocks/exchanges.html',
                           stock_exchanges=app.config.stock_exchanges,
                           search_data=search_data,
                           form=form,
                           search_query=exchange)


