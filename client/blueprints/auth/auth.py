from flask import Blueprint, render_template, redirect, url_for, request
from api_requests import users
from blueprints.auth.user import User
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('pages/login.html', err=None)

    else:
        username = request.form['username']
        password = request.form['password']

        if request.form.get('remember'):
            remember = True
        else:
            remember = False

        id = users.validate(username, password)

        if id is not None:
            user = User(id)
            login_user(user, remember=remember)
            return redirect(url_for('view.home'))
        else:
            err = {'username': username}
            return render_template('pages/login.html', err=err)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('pages/register.html', err=None)
    else:
        username = request.form['username']
        password = request.form['password']
        repeat_password = request.form['repeat_password']

        err = {'username': username}

        if password != repeat_password:
            err['err'] = 'password'
            return render_template('pages/register.html', err=err)
        else:
            if users.create(username, password):
                return render_template('pages/success.html')
            else:
                err['err'] = 'username'
                return render_template('pages/register.html', err=err)
