from requests import post, get

class Users():
    api_url = None

    def __init__(self, url_file):
            #get api_url
            with open(url_file, 'r', encoding = 'utf-8') as file:
                line = file.read()

            self.api_url = line.rstrip()

    def get_username(self, id):
        try:
            response = get('{url}/users/{id}'.format(url = self.api_url, id = id))
            response = response.json()
            return response['username']
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
                print(response['validated'])
                return response['user_id']
            else:
                return None
        except:
            return None
