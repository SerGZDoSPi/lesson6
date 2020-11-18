from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Base action'

@app.route('/Zubkov')
def v2():
    return 'Hello from CI with GitHub Actions by Zubkov'
