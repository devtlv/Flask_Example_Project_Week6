from flask import Blueprint, flash, render_template, request, current_app as app

from stocks_website.users.forms import LoginForm
from stocks_website.forms import SearchForm

users_routes = Blueprint('users', __name__, template_folder='templates')


@users_routes.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if False:
            pass
        else:
            flash('Wrong username or password.', 'error')
    elif request.method == 'POST':
        flash('Please input both username and password!', 'error')

    return render_template('users/login.html',
                           stock_exchanges=app.config.stock_exchanges,
                           form=SearchForm(),
                           login_form=form)
