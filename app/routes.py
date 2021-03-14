"""
This module provides routes for the home login and sign up pages.
"""
from flask import render_template, url_for, redirect, request,flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User

@app.route('/')
@app.route('/home')
@login_required
def home():
    """
    Provides funcionality for the home page route.
    """
    title = 'Home Page'
    return render_template('home.html', title=title)
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Provides funcionality for the login page.
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('home')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)
@app.route('/logout')
def logout():
    """
    Redirects the user to the home page in case the user logs out.
    """
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Povides funcionality for the sign up  page.
    """

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have been registered successfully!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
