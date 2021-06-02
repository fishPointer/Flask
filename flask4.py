from flask import Flask, render_template
from forms import signupForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'breadnetkeygen'


@app.route('/')
def home():
    form = signupForm()
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run()