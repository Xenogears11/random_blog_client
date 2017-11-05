from flask_login import UserMixin
from api_requests.users import Users
from flask_login import LoginManager

class User(UserMixin):
    username = 'Test'
    def __init__(self, id, username):
        self.id = id
        self.username = username

login_manager = LoginManager()
users = Users('api_url.txt')

@login_manager.user_loader
def load_user(id):
    username = users.get_username(id)
    return User(id, username)
