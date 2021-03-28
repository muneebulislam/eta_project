"""
This module provides routes for the home login and sign up pages.
"""
from flask import render_template, url_for, redirect, request,flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.recipe_construct import Recipe
from app.models import Recipe_db
from app.models import User

@app.route('/')
@app.route('/home')
@login_required
def home():
    """
    Provides functionality for the home page route.
    """
    title = 'Home Page'
    return render_template('home.html', title=title)
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Provides functionality for the login page.
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    Provides functionality for the sign up  page.
    """

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have been registered successfully!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/recipe_search', methods=['GET', 'POST'])
@login_required
def recipe_search():
    APP_ID = "a8ee5e3a"  # Put your app id for edamam api
    APP_KEY = "a5af30bf418171d4c205bb8c27cb02f2"  # Put your app key for edamam api

    NUTRITION_ID = "70dc1ef4"
    NUTRITION_KEY = "aeff761abf4758bc4076d53add38585e"

    search = "chicken"
    if request.method == 'POST':
        result = request.form
        search = result["Search Recipe"]

    recipe_app = Recipe(APP_ID, APP_KEY, NUTRITION_ID, NUTRITION_KEY)
    recipe_list = recipe_app.run_search_query(search)


    return render_template("recipe_display.html", recipe_list=recipe_list )

@app.route('/nutrients_search', methods=['GET', 'POST'])
@login_required
def nutrients_search():
    APP_ID = "a8ee5e3a"  # Put your app id for edamam api
    APP_KEY = "a5af30bf418171d4c205bb8c27cb02f2"  # Put your app key for edamam api

    NUTRITION_ID = "70dc1ef4"
    NUTRITION_KEY = "aeff761abf4758bc4076d53add38585e"

    search = "a cup of coke"
    if request.method == 'POST':
        result = request.form
        search = result["Search Nutrients"]

    recipe_app = Recipe(APP_ID, APP_KEY, NUTRITION_ID, NUTRITION_KEY)
    nutrients_list = recipe_app.run_nutrition_query(search)

    return render_template("nutrient_display.html", nutrients_list=nutrients_list)

@app.route("/save_recipe", methods=["GET", "POST"])
def save_recipe():
    saved_recipe= None
    if request.form:
        try:
            current_recipe = Recipe_db(recipe_title=request.form.get("recipe_title"), recipe_url = request.form.get("recipe_url"))
            db.session.add(current_recipe)
            db.session.commit()
        except Exception as e:
            print("Failed to add Recipe")
            print(e)
    # saved_recipe = Recipe_db.query.all()
    # return render_template("saved_recipes.html", saved_recipe = saved_recipe)
    return redirect(url_for("recipe_search"))

@app.route('/saved_recipes', methods = ['GET','POST'])
@login_required
def saved_recipes():
    saved_recipe = Recipe_db.query.all()
    return render_template("saved_recipes.html", saved_recipe = saved_recipe)

@app.route("/delete", methods=["POST"])
def delete():
   
    title = request.form.get("title")
    recipe = Recipe_db.query.filter_by(recipe_title=title).first()
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("saved_recipes"))


