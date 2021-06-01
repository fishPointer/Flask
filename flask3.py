from flask import Flask, render_template #add render_template to call .html files in the /templates directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('blog.html', author = "Bob", sunny=False) #you can pass a variable declaration into the parameters of the function and it will reference that in the html file's {{var}} calls
    # make sure you return the output of render_template, and then simply call the html file in /templates

@app.route('/blog')
def blog():
    posts = [{'title': 'Technology Time', 'author': 'Ian'}, {'title': 'Brainspasms', 'author':'Eein'}]
    return render_template('blog.html', author = "Jim", sunny=True, posts=posts)


if __name__ == '__main__':
    app.run()