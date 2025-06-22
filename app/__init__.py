import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Perry Chien", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    hobby_items = [
        {'title': 'Soccer', 'img': 'soccer.jpg'},
        {'title': 'Music', 'img': 'music.jpg'},
        {'title': 'Video Games', 'img': 'video_games.png'}
    ]
    return render_template('hobbies.html', title="Hobbies", hobbies=hobby_items, url=os.getenv("URL"))
