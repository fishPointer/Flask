# Basic Hello World for Flask. Creates a server at localhost:5000

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test8.db'

#Initalize the db
db = SQLAlchemy(app) #pass in the flask app

#Create db model
class Chan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), default='Anonymous')
    message = db.Column(db.String(16), nullable=False, default='hahaah')
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, message):
        self.name = name
        self.message = message

    #Function to return string on db add. returns name and entry number
    def __repr__(self):
        return '<Name %r>' % self.id 

class aChan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), default='Anonymous')
    message = db.Column(db.String(16), nullable=False, default='hahaah')
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, message):
        self.name = name
        self.message = message

    #Function to return string on db add. returns name and entry number
    def __repr__(self):
        return '<Name %r>' % self.id 

db.create_all()
# VERY IMPORTANT COMMAND APPARENTLY




posts=[]

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/h/')
def hentai():
    return render_template('hentai.html')

@app.route('/delete/<int:id>')
def delete(id):
    deleted_name = Chan.query.get_or_404(id) 
    try:
        db.session.delete(deleted_name)
        db.session.commit()
        return redirect('/posts')
    except:
        return "FaT Error Big Boy"

@app.route('/update/<int:id>', methods=["POST", "GET"])
def update(id):
    updated_name = Chan.query.get_or_404(id) 
    if request.method == "POST":
        updated_name.name = request.form["name"]
        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return "FaT Error Big Boy"
    else:
        return render_template("update.html", updated_name=updated_name)



@app.route('/posts', methods=["POST", "GET"])
def posts():

    boardurl = '/posts'
    if request.method == "POST":
        post_name = request.form['name']
        post_message = request.form['message']

        if not post_name:
            post_name = 'Anonymous'
        if not post_message:
            return "Please Enter Message"
        newchan = Chan(post_name, post_message)


        try:
            #db.session.add(new_post_username)
            db.session.add(newchan)
            db.session.commit()
            return redirect("/posts")
        except:
            return "There was an error, dickweed"
    else:
        chans = Chan.query.order_by(Chan.timestamp)
        return render_template('posts.html', chans=chans, url=boardurl)

@app.route('/board2', methods=["POST", "GET"])
def board2():

    boardurl = '/board2'
    if request.method == "POST":
        post_name = request.form['name']

        post_message = request.form['message']
        newchan = aChan(post_name, post_message)


        try:
            #db.session.add(new_post_username)
            db.session.add(newchan)
            db.session.commit()
            return redirect("/board2")
        except:
            return "There was an error, dickweed2"
    else:
        achans = aChan.query.order_by(aChan.timestamp)
        return render_template('posts.html', chans=achans, url=boardurl)



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
