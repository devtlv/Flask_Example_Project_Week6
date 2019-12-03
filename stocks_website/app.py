from flask import Flask
from flask_bootstrap import Bootstrap

from stocks_website import routes
from stocks_website.exchanges import get_stock_exchanges
from stocks_website.stocks import routes as stocks_routes


def create_app():
    app = Flask(__name__)
    app.config.world_trading_data_api_token = 'CfKzuYYPqeekR95Ud2Hime7E8cMxz6FgspmUWwbDQiavYJ0Tk55fEHAHpHeN'
    app.config.stock_exchanges = get_stock_exchanges(api_token=app.config.world_trading_data_api_token)

    Bootstrap(app)

    return app


app = create_app()

app.register_blueprint(routes.main_routes)
app.register_blueprint(stocks_routes.stocks_routes)
