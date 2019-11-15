from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Radio'}
    posts = [
        {
            'author': {'username': 'Radio'},
            'body': 'why is everyone not bothered about mother earth'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'save earth for the next generation'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)