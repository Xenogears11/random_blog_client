from requests import get, post
import sys

class Blog():
    api_url = None

    def __init__(self, url_file):
            #get api_url
            with open(url_file, 'r', encoding = 'utf-8') as file:
                line = file.read()

            self.api_url = line.rstrip()

    def get_post(self, post_id):
        try:
            data = get('{url}/posts/{id}'.format(url = self.api_url, id = post_id))
            return data.json()
        except:
            return None

    def get_home(self):
        try:
            data = get('{url}/all'.format(url = self.api_url))
            return data.json()
        except:
            return None

    def get_category(self, category_id):
        try:
            data = get('{url}/all/{id}'.format(url = self.api_url, id = category_id))
            return data.json()
        except:
            return None

    def get_categories(self):
        try:
            data = get('{url}/categories'.format(url = self.api_url))
            return data.json()
        except:
            return None

    def new_post(self, header, content, author, categories):
        data = {
            'header' : header,
            'content' : content,
            'author' : author,
            'categories' : [categories]
        }
        try:
            r = post('{url}/posts'.format(url = self.api_url), data = data)
            j = r.json()
            print(j['id'])
            return j['id']
        except:
            return None
