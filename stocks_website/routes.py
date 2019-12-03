from flask import Blueprint, render_template, current_app as app

main_routes = Blueprint('main', __name__, 'templates/')


@main_routes.route('/')
def index():
    return render_template('index.html',
                           stock_exchanges=app.config.stock_exchanges)
