import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    con = get_db()
    posts = con.execute('SELECT * FROM posts').fetchall()
    con.close()
    return render_template('index.html', posts=posts)


def get_db():
    con = sqlite3.connect('db.sqlite3')
    con.row_factory = sqlite3.Row
    
    return con