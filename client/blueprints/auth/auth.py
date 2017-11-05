from flask import Blueprint, render_template, redirect, abort, url_for, request
from jinja2 import TemplateNotFound
from api_requests.users import Users
from blueprints.auth.user import User
from flask_login import login_user, logout_user

auth = Blueprint('auth', __name__, template_folder = 'templates')
users = Users('api_url.txt')

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('pages/login.html')

    else:
        username = request.form['username']
        password = request.form['password']
        print(username, password)

        id = users.validate(username, password)
        print(id)

        if id != None:
            username = users.get_username(id)
            user = User(id, username)
            login_user(user)
            return redirect(url_for('view.home'))
        else:
            return abort(401)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('view.home'))
