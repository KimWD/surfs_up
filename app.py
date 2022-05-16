# import flask
from flask import Flask

#create new flask app Instance called app
app = Flask(__name__)

#Create the route
@app.route('/')
def hello_world():
    return 'Hello world'
    
