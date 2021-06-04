# Basic Hello World for Flask. Creates a server at localhost:5000

from flask import Flask, render_template, request

app = Flask(__name__)

posts=[]

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/h/')
def hentai():
    return render_template('hentai.html')

@app.route('/form')
def form():

    return render_template('form.html')

@app.route('/submit', methods=["POST"])
def submission():
    username = request.form.get("username")
    if not username:
        username = "Anonymous"
    subject = request.form.get("subject")
    if not subject:
        subject = "None"
    message = request.form.get("message")

    if not message:
        error_statement = "Please fill out the Message field..."
        return render_template('form.html', username=username, subject=subject, message=message, posts=posts, error_statement=error_statement)

    posts.append(f"Name: {username} - Subject: {subject} | {message}")
    return render_template('submission.html', username=username, subject=subject, message=message, posts=posts)

if __name__ == '__main__':
    app.run()
