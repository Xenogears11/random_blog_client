from flask import Flask
from blueprints.view.view import view
from blueprints.auth.auth import auth
from blueprints.error.error import error
from blueprints.auth.user import login_manager

app = Flask(__name__)

# blueprints
app.register_blueprint(view)
app.register_blueprint(auth)
app.register_blueprint(error)

# Login manager
with open('res/secret.txt', 'r', encoding='utf-8') as file:
    line = file.read()
secret = line.rstrip()
app.config.update(
    SECRET_KEY=secret
)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
