from requests import get, post, delete, put, codes
import sys

class Blog():
    api_url = None

    def __init__(self, url_file):
            #get api_url
            with open(url_file, 'r', encoding = 'utf-8') as file:
                line = file.read()

            self.api_url = line.rstrip()

    def get_post(self, id):
        try:
            data = get('{url}/posts/{id}'.format(url = self.api_url, id = id))
            return data.json()
        except:
            return None

    def get_home(self):
        try:
            data = get('{url}/blog/home'.format(url = self.api_url))
            return data.json()
        except:
            return None

    def get_category(self, id):
        try:
            data = get('{url}/blog/category/{id}'.format(url = self.api_url, id = id))
            return data.json()
        except:
            return None

    def get_categories(self):
        try:
            data = get('{url}/categories'.format(url = self.api_url))
            return data.json()
        except:
            return None

    def get_edit_page(self, id):
        try:
            data = get('{url}/blog/edit_post/{id}'.format(url = self.api_url, id = id))
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
            return j['id']
        except:
            return None

    def delete_post(self, id):
        try:
            response = delete('{url}/posts/{id}'.format(url = self.api_url, id = id))

            if response.status_code == codes.ok:
                return True
            else:
                return False

        except:
            return False

    def edit_post(self, id, header, content, author, categories):
        data = {
            'header' : header,
            'content' : content,
            'author' : author,
            'categories' : [categories]
        }
        try:
            response = put('{url}/posts/{id}'.format(url = self.api_url, id = id), data = data)

            if response.status_code == codes.ok:
                return id
            else:
                return None

        except:
            return None

    def restore_post(self, id):
        try:
            response = put('{url}/posts/{id}/restore'.format(url = self.api_url, id = id))

            if response.status_code == codes.ok:
                return id
            else:
                return None

        except:
            return None