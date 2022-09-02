import sqlite3
from turtle import title
from werkzeug.exceptions import abort
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'CHAVE'

@app.route('/')
def index():
    con = get_db()
    posts = con.execute('SELECT * FROM posts').fetchall()
    con.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
    
        if not title:
            flash('Title is required')
        else:
            con = get_db()
            con.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            con.commit()
            con.close()
            return redirect(url_for('index'))
    return render_template('create.html')

def get_db():
    con = sqlite3.connect('db.sqlite3')
    con.row_factory = sqlite3.Row

    return con


def get_post(post_id:int):
    con = get_db()
    post = con.execute('SELECT * FROM posts where id = ?', (post_id,)).fetchone()
    con.close()
    if post is None:
        abort(404)
    return post
