
from flask import Flask, render_template, request, redirect
from peewee import * 
from models import Post

app = Flask(__name__)

@app.route('/') 
def mike():
    all_posts = Post.select()
    return render_template("index.html", posts=all_posts)

@app.route('/create/', methods = ('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['title']
        name = request.form['name']
        email = request.form['email']

        Post.create(
            title = title,
            description = description,
            name = name,
            email = email

        )
        return redirect('/')
    return render_template('create.html')

@app.route('/bye')
def ex():
    return '<h1>bye</h1>'

if __name__ == "__main__":
    app.run(debug=True)


