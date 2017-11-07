from requests import post, get, codes
from flask_login import current_user
from flask import abort
from functools import wraps
from api_requests.blog import Blog

class Users():
    api_url = None

    def __init__(self, url_file):
            #get api_url
            with open(url_file, 'r', encoding = 'utf-8') as file:
                line = file.read()

            self.api_url = line.rstrip()

    def get_user(self, id):
        try:
            response = get('{url}/users/{id}'.format(url = self.api_url, id = id))
            response = response.json()
            return {
                'username' : response['username'],
                'is_admin' : response['is_admin']
                }
        except:
            return None

    def validate(self, username, password):
        data = {
            'username' : username,
            'password' : password
        }

        try:
            response = post('{url}/auth'.format(url = self.api_url), data = data)
            response = response.json()

            if response['validated'] == True:
                return response['user_id']
            else:
                return None
        except:
            return None

    def create(self, username, password):
        data = {
            'username' : username,
            'password' : password
        }

        try:
            response = post('{url}/users'.format(url = self.api_url), data = data)

            if response.status_code == codes.ok:
                return True
            else:
                return False
        except:
            return False

blog = Blog('api_url.txt')

def access_check(func):
    @wraps(func)
    def wrapper(id, *args, **kwargs):
        author_id = blog.get_author(id)
        if current_user.is_admin or int(current_user.id) == int(author_id):
            return func(id, *args, **kwargs)
        else:
            abort(403)

    return wrapper
