from flask import Blueprint, render_template, redirect, abort, url_for, request
from jinja2 import TemplateNotFound
from api_requests.users import Users
from blueprints.auth.user import User
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__, template_folder = 'templates')
users = Users('api_url.txt')

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('pages/login.html')

    else:
        username = request.form['username']
        password = request.form['password']

        if request.form.get('remember'):
            remember = True
        else:
            remember = False

        id = users.validate(username, password)

        if id != None:
            user = User(id)
            login_user(user, remember = remember)
            return redirect(url_for('view.home'))
        else:
            return abort(401)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('view.home'))

@auth.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('pages/register.html')
    else:
        username = request.form['username']
        password = request.form['password']
        repeat_password = request.form['repeat_password']

        if password != repeat_password:
            return render_template('passwords_not_match.html')
        else:
            if users.create(username, password):
                return render_template('pages/success.html')
            else:
                return render_template('username_exists.html')
