from flask import Flask  # importing flask

def create_app(): 
    app = Flask(__name__) # Create an app instance from Flask. Be sure to pass it the special dunder variable

    #home route
    @app.route('/') 
    def hello(): 
        return 'Hello, PetFax!'

    # pets index route
    @app.route('/pets')
    def pets(): 
        return 'These are our pets available for adoption!'

    return app
