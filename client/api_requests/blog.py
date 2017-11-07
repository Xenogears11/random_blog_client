from requests import get, post, delete, put, codes
import sys
import mistune

class Blog():
    api_url = None
    renderer = mistune.Renderer(hard_wrap = True)
    markdown = mistune.Markdown(renderer = renderer)

    def __init__(self, url_file):
            #get api_url
            with open(url_file, 'r', encoding = 'utf-8') as file:
                line = file.read()

            self.api_url = line.rstrip()

    def get_post(self, id):
        try:
            data = get('{url}/posts/{id}'.format(url = self.api_url, id = id))
            data = data.json()
            data['content'] = self.markdown(data['content'])
            return data
        except:
            return None

    def get_home(self, quantity, from_id = None, newer = None):
        req = {
            'quantity':quantity,
            'from_id':from_id
        }
        if newer != None:
            req['newer'] = 'true'

        try:
            data = get('{url}/blog/home'.format(url = self.api_url), data = req)
            data = data.json()
            for post in data['posts']:
                post['content'] = self.markdown(post['content'])
            return data
        except:
            return None

    def get_category(self, id, quantity, from_id = None, newer = None):
        req = {
            'quantity':quantity,
            'from_id':from_id
        }
        if newer != None:
            req['newer'] = 'true'

        try:
            data = get('{url}/blog/category/{id}'.format(url = self.api_url, id = id), data = req)
            data = data.json()
            for post in data['posts']:
                post['content'] = self.markdown(post['content'])
            return data
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

    def new_post(self, header, content, author_id, categories):
        data = {
            'header' : header,
            'content' : content,
            'author_id' : author_id,
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

    def edit_post(self, id, header, content, categories):
        data = {
            'header' : header,
            'content' : content,
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

    def get_author(self, id):
        try:
            response = get('{url}/posts/{id}/author'.format(url = self.api_url, id = id))

            response = response.json()
            return response['author_id']
        except:
            return None
