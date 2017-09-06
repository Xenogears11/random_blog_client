from flask import Flask
from blueprints.view.view import view

app = Flask(__name__)
app.register_blueprint(view)
