from flask_login import UserMixin
from api_requests.users import Users
from flask_login import LoginManager

login_manager = LoginManager()
users = Users('api_url.txt')

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.load()

    def load(self):
        data = users.get_user(self.id)
        self.username = data['username']
        self.is_admin = data['is_admin']

@login_manager.user_loader
def load_user(id):
    return User(id)
