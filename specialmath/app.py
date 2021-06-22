from flask import Flask

from specialmath import special_math

app = Flask(__name__)


@app.route('/')
def invalid_path_root():
    return 'Call with a valid number in the URL.' \
           ' Example: http://127.0.0.1:5000/specialmath/7'


@app.route('/<path:some_string>')
def invalid_path(some_string):
    return invalid_path_root()


@app.route('/specialmath/<int:num>')
def valid_path(num):
    return special_math(num)


if __name__ == '__main__':
    app.run()
