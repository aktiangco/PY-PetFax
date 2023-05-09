# Activity: PetFax
#! cd into: day5
#! cd into: PY-PetFax
#! To check: python3 app.py

# config                    
from flask import Flask # importing flask
app = Flask(__name__) # Create an app instance from Flask. Be sure to pass it the special dunder variable

# index route
@app.route('/')
def index():
    return 'Hello, this is PetFax!'

# pets index route
@app.route('/pets')
def pets(): 
    return 'These are our pets available for adoption!'

