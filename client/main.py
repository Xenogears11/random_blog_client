from flask import Flask
from blueprints.view.view import view
from blueprints.auth.auth import auth
from blueprints.error.error import error
from blueprints.auth.user import login_manager


app = Flask(__name__)

#blueprints
app.register_blueprint(view)
app.register_blueprint(auth)
app.register_blueprint(error)
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx'
)

#login manager
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
