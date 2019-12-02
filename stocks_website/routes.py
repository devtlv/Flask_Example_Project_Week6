from flask import Blueprint, render_template

from stocks_website.exchanges import get_stock_exchanges

main_routes = Blueprint('main', __name__, 'templates/')


@main_routes.route('/')
def index():
    return render_template('index.html',
                           stock_exchanges=get_stock_exchanges())
