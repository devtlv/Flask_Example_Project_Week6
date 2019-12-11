from flask import Blueprint, flash, render_template, request, current_app as app, redirect
from sqlalchemy import func

from stocks_website.users.models import User
from stocks_website.users.forms import LoginForm, RegisterForm
from stocks_website.forms import SearchForm
from stocks_website.users.repositories import UsersRepository

users_routes = Blueprint('users', __name__, template_folder='templates')


@users_routes.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(email=form.email,
                                 password=func.digest(form.password,
                                                      'sha256')).first()
        if user:
            return redirect('/')
        else:
            flash('Wrong username or password.', 'error')
    elif request.method == 'POST':
        flash('Please input both username and password!', 'error')

    return render_template('users/login.html',
                           stock_exchanges=app.config.stock_exchanges,
                           form=SearchForm(),
                           login_form=form)


@users_routes.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        repo = UsersRepository()
        repo.register(form.email.data,
                      form.first_name.data,
                      form.last_name.data,
                      form.password.data,
                      form.country.data,
                      form.sex.data)
        return redirect('/')
    else:
        flash("ERROR", 'error')
    return render_template('users/register.html',
                           stock_exchanges=app.config.stock_exchanges,
                           form=SearchForm(),
                           register_form=form
                           )
