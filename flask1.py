# Basic Hello World for Flask. Creates a server at localhost:5000

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'I am Flask'

if __name__ == '__main__':
    app.run()
