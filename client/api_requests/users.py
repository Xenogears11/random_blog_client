from requests import post, get, codes

# get api_url
with open('res/api_url.txt', 'r', encoding='utf-8') as file:
    line = file.read()
api_url = line.rstrip()


def get_user(id):
    try:
        response = get('{url}/users/{id}'.format(url=api_url, id=id))
        response = response.json()
        return {
            'username': response['username'],
            'is_admin': response['is_admin']
        }
    except:
        return None


def validate(username, password):
    data = {
        'username': username,
        'password': password
    }

    try:
        response = post('{url}/auth'.format(url=api_url), data=data)
        response = response.json()

        if response['validated']:
            return response['user_id']
        else:
            return None
    except:
        return None


def create(username, password):
    data = {
        'username': username,
        'password': password
    }

    try:
        response = post('{url}/users'.format(url=api_url), data=data)

        if response.status_code == codes.ok:
            return True
        else:
            return False
    except:
        return False

