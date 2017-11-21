from flask import Blueprint, render_template
from blueprints.view.view import view
from blueprints.auth.auth import auth

error = Blueprint('error', __name__, template_folder='templates')


@view.errorhandler(401)
@auth.errorhandler(401)
def unauthorized(e):
    return render_template('401.html')


@view.errorhandler(403)
@auth.errorhandler(403)
def unauthorized(e):
    return render_template('403.html')


@view.errorhandler(404)
@auth.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
