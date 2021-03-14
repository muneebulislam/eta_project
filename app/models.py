"""
This module creates User objects for the databse. It also use build in modules like flask-login and werkzeug.security.
To set password and check password. It also creates a hash-code for the password to provide security for the system 
from some unknown attacks. Password is not in string form but is hashed.
"""
from app import db
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
class User(UserMixin, db.Model):
    """
    Creates a User object for the using database model.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    def __repr__(self):
        return '<User  username: {} email: {}  hashed passowrd: {}>'.format(self.username,self.email,self.password_hash)
    def set_password(self, password):
        """
        Sets password for a new user. 
        @passowrd: password entered by the user.
        @return: returns a hash-code for the password.
        """
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
@login.user_loader
def load_user(id):
    """
    Used to get infomation for a user in database.
    @id: id of the user
    @return: returns the User for the given id.
    """
    return User.query.get(int(id))