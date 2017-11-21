from requests import get, post, delete, put, codes
import mistune
from flask_login import current_user
from flask import abort
from functools import wraps


# mistune renderer for markdown
renderer = mistune.Renderer(hard_wrap=True)
markdown = mistune.Markdown(renderer=renderer)

# get api_url
with open('res/api_url.txt', 'r', encoding='utf-8') as file:
    line = file.read()
api_url = line.rstrip()


def get_post(id):
    try:
        data = get('{url}/posts/{id}'.format(url=api_url, id=id))
        data = data.json()
        data['content'] = markdown(data['content'])
        return data
    except:
        return None


def get_home(quantity, from_id=None, newer=None):
    req = {
        'quantity': quantity,
        'from_id': from_id
    }
    if newer is not None:
        req['newer'] = 'true'

    try:
        data = get('{url}/blog/home'.format(url=api_url), data=req)
        data = data.json()
        for post in data['posts']:
            post['content'] = markdown(post['content'])
        return data
    except:
        return None


def get_category(id, quantity, from_id=None, newer=None):
    req = {
        'quantity': quantity,
        'from_id': from_id
    }
    if newer is not None:
        req['newer'] = 'true'

    try:
        data = get('{url}/blog/category/{id}'.format(url=api_url, id=id), data=req)
        data = data.json()
        for post in data['posts']:
            post['content'] = markdown(post['content'])
        return data
    except:
        return None


def get_categories():
    try:
        data = get('{url}/categories'.format(url=api_url))
        return data.json()
    except:
        return None


def get_edit_page(id):
    try:
        data = get('{url}/blog/edit_post/{id}'.format(url=api_url, id=id))
        return data.json()
    except:
        return None


def new_post(header, content, author_id, categories):
    data = {
        'header': header,
        'content': content,
        'author_id': author_id,
        'categories': [categories]
    }

    try:
        r = post('{url}/posts'.format(url=api_url), data=data)
        j = r.json()
        return j['id']
    except:
        return None


def delete_post(id):
    try:
        response = delete('{url}/posts/{id}'.format(url=api_url, id=id))

        if response.status_code == codes.ok:
            return True
        else:
            return False

    except:
        return False


def edit_post(id, header, content, categories):
    data = {
        'header': header,
        'content': content,
        'categories': [categories]
    }
    try:
        response = put('{url}/posts/{id}'.format(url=api_url, id=id), data=data)

        if response.status_code == codes.ok:
            return id
        else:
            return None

    except:
        return None


def restore_post(id):
    try:
        response = put('{url}/posts/{id}/restore'.format(url=api_url, id=id))

        if response.status_code == codes.ok:
            return id
        else:
            return None

    except:
        return None


def get_author(id):
    try:
        response = get('{url}/posts/{id}/author'.format(url=api_url, id=id))

        response = response.json()
        return response['author_id']
    except:
        return None


def access_check(func):
    @wraps(func)
    def wrapper(id, *args, **kwargs):
        author_id = get_author(id)
        if current_user.is_admin or int(current_user.id) == int(author_id):
            return func(id, *args, **kwargs)
        else:
            abort(403)

    return wrapper
