from flask import Flask
from flask_bootstrap import Bootstrap

from stocks_website import routes
from stocks_website.stocks import routes as stocks_routes


def create_app():
    app = Flask(__name__)

    Bootstrap(app)

    return app


app = create_app()

app.register_blueprint(routes.main_routes)
app.register_blueprint(stocks_routes.stocks_routes)
