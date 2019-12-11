import os

from flask import Flask
from flask_bootstrap import Bootstrap

from stocks_website import routes
from stocks_website.database import db, migrate
from stocks_website.exchanges import StockExchangesRepository
from stocks_website.stocks import routes as stocks_routes
from stocks_website.users import routes as users_routes


def create_app():
    """App factory."""
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config.world_trading_data_api_token = 'CfKzuYYPqeekR95Ud2Hime7E8cMxz6FgspmUWwbDQiavYJ0Tk55fEHAHpHeN'
    repository = StockExchangesRepository(api_token=app.config.world_trading_data_api_token)
    app.config.stock_exchanges = repository.get_stock_exchanges()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres://postgres@localhost/postgres')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    from stocks_website.users.models import User

    Bootstrap(app)

    return app


app = create_app()

app.register_blueprint(routes.main_routes)
app.register_blueprint(stocks_routes.stocks_routes)
app.register_blueprint(users_routes.users_routes)
