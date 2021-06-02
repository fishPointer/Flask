from flask import Flask, render_template, redirect, request, url_for
from forms import signupForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'breadnetkeygen'


@app.route('/blog')
def blog():
    posts = [{'title': 'Technology Time', 'author': 'Ian'}, {'title': 'Brainspasms', 'author':'Eein'}]
    return render_template('blog2.html', author = "Jim", sunny=True, posts=posts)

@app.route('/')
def home():
    posts = [{'title': 'Technology Time', 'author': 'Ian'}, {'title': 'Brainspasms', 'author':'Eein'}]
    return render_template('blog2.html', author = "HOME", sunny=True, posts=posts)

@app.route('/signup', methods=['GET', 'POST']) # This part isn't working, not sure why. Moving on
def signup():
    form = signupForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run()