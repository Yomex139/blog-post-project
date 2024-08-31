import requests
import datetime
from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = requests.get(url=' https://api.npoint.io/5d1cc9b914439c7446a8').json()
date = datetime.datetime.now().date().strftime('%B %d, %Y')


@app.route("/")
def homepage():
    return render_template('index.html', all_post=posts, posted=date)


@app.route("/about")
def About():
    return render_template('about.html')


@app.route("/contact")
def Contact():
    return render_template('contact.html')


@app.route("/post/<int:index>")
def post(index):
    requested = None
    for posted in posts:
        if posted['id'] == index:
            requested = posted
            print(requested)
    return render_template('post.html', post=requested, date=date)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='localhost')
