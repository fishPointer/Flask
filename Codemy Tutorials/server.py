# Basic Hello World for Flask. Creates a server at localhost:5000

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test3.db'

#Initalize the db
db = SQLAlchemy(app) #pass in the flask app

#Create db model
class Chan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    #message = db.Column(db.String(16), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    #Function to return string on db add. returns name and entry number
    def __repr__(self):
        return '<Name %r>' % self.id 

db.create_all()





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

    if request.method == "POST":
        post_name = request.form['name']
        new_post_username = Chan(name=post_name)

        #post_message = request.form['message']
        #new_post_message = Chan(message=post_message)

        try:
            db.session.add(new_post_username)
            db.session.commit()
            return redirect("/posts")
        except:
            return "There was an error, dickweed"
    else:
        chans = Chan.query.order_by(Chan.timestamp)
        return render_template('posts.html', chans=chans)



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
