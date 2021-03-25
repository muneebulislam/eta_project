"""
This module perform the functionality of creating the Login forms and Sign up forms.
It makes use of the functionality of built in wtforms modules adopted for the 
Flask applications. 
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField 
from wtforms.validators import DataRequired,ValidationError, Email, EqualTo
from app.models import User
class LoginForm(FlaskForm):
    """
    Creates components for a login form for flask app.
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class RegistrationForm(FlaskForm):
    """
    This class creates components for a Sign up form
    """
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """
        Validates the username. If the username exists already then returns an error message.
        @username: username for a given user. 
        """
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username because this username is already taken.')

    def validate_email(self, email):
        """
        Validates the email address of the user. If the email address is registered with some other user in the
        database then returns an error message in string form.
        @email: email address of the user.
        """
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address because this email address is already registered with some other user.')