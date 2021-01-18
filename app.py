from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World XXX!'

@app.route('/flaskie')
def index():
    return 'Hello, World XXX!'