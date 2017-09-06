from flask import Blueprint, render_template, redirect, abort, url_for
from jinja2 import TemplateNotFound
from api_requests import Blog

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

@view.route('/post/new')
def new_post():
    try:
        return redirect(url_for('view.soon'))
    except TemplateNotFound:
        abort(404)

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

@view.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
