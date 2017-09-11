from flask import Blueprint, render_template, redirect, abort, url_for, request
from jinja2 import TemplateNotFound
from api_requests.blog import Blog
import sys

view = Blueprint('view', __name__, template_folder = 'templates')
blog = Blog('api_url.txt')

@view.route('/')
def main():
    return redirect(url_for('view.home'))

@view.route('/home')
def home():
    quantity = 3
    from_id = request.args.get('from_id')
    previous = request.args.get('previous')
    data = blog.get_home(quantity, from_id, previous)
    try:
        return render_template('pages/home.html', data = data)
    except:
        abort(404)

@view.route('/post/new', methods=['POST', 'GET'])
def new_post():
    data = None
    if request.method == 'GET':
        data = blog.get_categories()
        try:
            return render_template('pages/new_post.html', data = data)
        except:
            abort(404)

    else:
        try:
            post_id = blog.new_post(
                      request.form['header'],
                      request.form['content'],
                      request.form['author'],
                      request.form['category'])
            return redirect(url_for('view.post', id = post_id))
        except:
            abort(400)

@view.route('/post/<int:id>')
def post(id):
    data = blog.get_post(id)
    try:
        return render_template('pages/post.html', data = data)
    except:
        abort(404)

@view.route('/post/<int:id>/edit', methods=['GET', 'POST'])
def edit_post(id):
    if request.method == 'GET':
        data = blog.get_edit_page(id)
        try:
            return render_template('pages/edit_post.html', data = data)
        except:
            abort(404)

    else:
        id = blog.edit_post(id,
             request.form['header'],
             request.form['content'],
             request.form['author'],
             request.form['category'])
        try:
            return redirect(url_for('view.post', id = id))
        except:
            abort(404)

@view.route('/post/<int:id>/delete')
def delete_post(id):
    response = blog.delete_post(id)

    if response:
        try:
            return render_template('pages/post_deleted.html', id = id)
        except:
            abort(404)

    else:
        abort(404)

@view.route('/post/<int:id>/restore')
def restore_post(id):
    post_id = blog.restore_post(id)
    if post_id != None:
        try:
            return redirect(url_for('view.post', id = post_id))
        except:
            return abort(404)

    else:
        return abort(404)

@view.route('/category/<int:id>')
def category(id):
    quantity = 3
    from_id = request.args.get('from_id')
    previous = request.args.get('previous')

    data = blog.get_category(id, quantity, from_id, previous)
    #try:
    return render_template('pages/category.html', data = data)
    #except:
        #abort(404)

@view.route('/categories')
def categories():
    try:
        return redirect(url_for('view.soon'))
    except:
        abort(404)

@view.route('/about')
def about():
    try:
        return render_template('pages/about.html')
    except:
        abort(404)

@view.route('/soon')
def soon():
    try:
        return render_template('pages/soon.html')
    except:
        abort(404)

@view.route('/memes')
def memes():
    return render_template('pages/memes.html')

@view.errorhandler(404)
def page_not_found(e):
    return render_template('error_pages/404.html')
