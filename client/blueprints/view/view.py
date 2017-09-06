from flask import Blueprint, render_template, redirect, abort, url_for, request
from jinja2 import TemplateNotFound
from api_requests.blog import Blog
import sys

view = Blueprint('view', __name__, template_folder = 'templates')
blog = Blog('api_url.txt')

@view.route('/')
def main():
    return redirect(url_for('view.home'))

@view.route('/post/<int:id>')
def post(id):
    data = blog.get_post(id)
    try:
        return render_template('post.html', data = data)
    except TemplateNotFound:
        abort(404)

@view.route('/post/new', methods=['POST', 'GET'])
def new_post():
    data = None
    if request.method == 'GET':
        data = blog.get_categories()
        try:
            return render_template('new_post.html', data = data)
        except TemplateNotFound:
            abort(404)

    else:
        try:
            data = blog.new_post(
                   request.form['header'],
                   request.form['content'],
                   request.form['author'],
                   request.form['category'])
            return redirect(url_for('view.post', id = data))
        except:


@view.route('/home')
def home():
    data = blog.get_home()
    try:
        return render_template('home.html', data = data)
    except TemplateNotFound:
        abort(404)

@view.route('/category/<int:id>')
def category(id):
    data = blog.get_category(id)
    try:
        return render_template('category.html', data = data)
    except TemplateNotFound:
        abort(404)

@view.route('/categories')
def categories():
    try:
        return redirect(url_for('view.soon'))
    except TemplateNotFound:
        abort(404)

@view.route('/about')
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)

@view.route('/soon')
def soon():
    try:
        return render_template('soon.html')
    except TemplateNotFound:
        abort(404)

@view.route('/memes')
def memes():
    return render_template('memes.html')

@view.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
