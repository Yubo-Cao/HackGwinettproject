from sqlite3.dbapi2 import IntegrityError
from flask import Flask, render_template;
import sqlite3;
import random;

app = Flask(__name__);

def get_db_conn():
    conn = sqlite3.connect("database.db");
    conn.row_factory = sqlite3.Row;
    return conn;

def get_post(post_id):
    conn =get_db_conn();
    post = conn.execute("select * from posts where id = ?",(post_id,));
    return post;

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/about')
def about():
    return render_template('about.html');

@app.route('/posts')
def posts():
    conn = get_db_conn();
    posts = conn.execute("select * from posts").fetchall();
    return render_template('posts.html',posts = posts);

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html',post = get_post(post_id));

@app.route('/join')
def join():
    return render_template('join.html');
    
if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = random.randint(2000,9000));