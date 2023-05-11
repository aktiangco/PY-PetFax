# config                    
from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()
POSTGRES = os.environ.get("POSTGRES") #to fetch from .env file
from flask_migrate import Migrate

# factory
def create_app():
    app = Flask(__name__)
    
    # Database Config
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    
    # to access to all built-in SQLAlchemy
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db) 
    

    # index route
    @app.route('/')
    def index(): 
        return 'Hello, PetFax!'

    # register pet blueprint 
    from . import pet 
    app.register_blueprint(pet.bp)
    
    # register fact blueprint
    from . import fact
    app.register_blueprint(fact.bp) 

    # return the app 
    return app
