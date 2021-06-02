from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class signupForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign Up')