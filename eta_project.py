"""
This module creates a flask shell context. We will not need to import the module first in the 
flask shell and then use it. We can access the variables like db, Use etc directly in the flask
shell.
"""
from app import app, db
from app.models import User
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
