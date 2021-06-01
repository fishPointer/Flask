# Routing Tutorial. add routes, and add variables to the path names for those routes

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'I am Flask'

@app.route('/thread')
def punk(): #/directory doesn't need to change function() name
    return 'This is the first Thread'

@app.route('/thread/<int:thread_id>') #pass variables into the route using <varname>
def threadpost(thread_id): #define the var in the page function
    return ('This is the nth Thread. N = ' + str(thread_id)) #define the var type using colon int:varname

@app.route('/post/<string:postcontent>')
def post(postcontent):
    return ('this is a post, the post reads: ' + postcontent)


if __name__ == '__main__':
    app.run()
