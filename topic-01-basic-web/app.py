from flask import url_for, Flask, render_template
from flask import request
from markupsafe import escape

app=Flask(__name__)


def do_the_login():
    return 'do the login'

def show_the_login_form():
    return 'show the login form'

@app.route('/hello/<name>/<int:num>')
def hello(name=None, num=0):
    return render_template('hello.html', person=name, count=num)



# with app.test_request_context('/hello', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method == 'POST'


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


def valid_login(username, password):
    return username == 'admin' and password == 'secret'

def log_the_user_in(username):
    return f'Logged in as {escape(username)}'



@app.route('/')
def index():
    return 'index'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

# @app.route('/post/testcss')
# def testcss():
#     return render_template('style.css')

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('static', filename='style.css'))
