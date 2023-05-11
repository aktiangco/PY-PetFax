from flask import ( Blueprint, render_template, request, redirect ) 
from . import models

bp = Blueprint('fact', __name__, url_prefix="/facts")

# to post new router
@bp.route('/new')
def new(): 
    return render_template('facts/new.html')

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method== 'POST':
        submitter = request.form['submitter']
        fact = request.form['fact']

        new_fact = models.Fact(submitter=submitter, fact=fact) #new_fact to the Flask-SQLAlchemy database session
        models.db.session.add(new_fact)
        models.db.session.commit() #Commit the database session, which will insert the data into the database.

        
        return redirect('/facts')
    
    results = models.Fact.query.all() # retrieve all query
  
    return render_template('facts/index.html', facts=results)
