from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Page!'
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    request.get_data()
    return 'Hello World'
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5060,
        debug=True
    )