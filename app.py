import sqlite3
from werkzeug.exceptions import abort
from flask import Flask, render_template

app = Flask(__name__)


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
