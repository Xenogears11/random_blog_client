from flask import Flask, render_template, redirect, url_for, abort
from requests import get
app = Flask(__name__)

#get api_url
with open('api_url.txt', 'r', encoding = 'utf-8') as file:
    line = file.read()
    api_url = line.rstrip()

@app.route('/')
def hello():
    return redirect(url_for('home'))

@app.route('/post/<int:id>')
def show_post(id):
    r = get(api_url + 'posts/get/' + str(id))
    try:
        post = r.json()
    except:
        abort(404)
    return render_template('post.html', post = post)

@app.route('/post/new')
def new_post():
    return redirect(url_for('soon'))

@app.route('/home')
def home():
    posts = get(api_url + 'posts/get')
    categories = get(api_url + 'categories/get')
    return render_template('home.html', posts = posts.json(), categories = categories.json())

@app.route('/category/<int:id>')
def category(id):
    category = get(api_url + 'categories/get/' + str(id))
    categories = get(api_url + 'categories/get')
    posts = get(api_url + 'posts/get', data = {'category_id':id})
    return render_template('category.html', posts = posts.json(), category = category.json(),
                            categories = categories.json())

@app.route('/categories')
def categories():
    return redirect(url_for('soon'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/soon')
def soon():
    return render_template('soon.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
