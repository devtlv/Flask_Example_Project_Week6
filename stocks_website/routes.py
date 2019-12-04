from flask import Blueprint, render_template, current_app as app

from stocks_website.forms import SearchForm
from stocks_website.stocks.repositories import StocksRepository

main_routes = Blueprint('main', __name__, 'templates/')


@main_routes.route('/')
def index():
    form = SearchForm()
    return render_template('index.html',
                           stock_exchanges=app.config.stock_exchanges,
                           form=form)


@main_routes.route('/search', methods=('GET', 'POST'))
def search():
    form = SearchForm()
    if form.validate_on_submit():
        repo = StocksRepository()
        search_data = repo.search(search_term=form.search_term.data)
        return render_template('stocks/exchanges.html',
                               stock_exchanges=app.config.stock_exchanges,
                               search_data=search_data,
                               form=form,
                               search_query=form.search_term)

    raise ValueError("Type a search term!")
