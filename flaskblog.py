from flask import Flask
# app instance
app = Flask(__name__)

# route decorators -> adds additional functionality to existing functions
@app.route('/')
def hello():
    return "<h1>Hello punk. lets bild a sports data backend. make code cool</h1>"

# only true if we run this script directly and not importing it