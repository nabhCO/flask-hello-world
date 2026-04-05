from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Nandini Bhat in 3308'
