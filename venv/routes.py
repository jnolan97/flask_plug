from venv import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required,login_user,current_user,logout_user
from flask_admin.contrib import sqla
from flask_admin import helpers, expose

# import forms
from venv.forms import UserInfoForm, LoginForm
#import models
from venv.models import User, check_password_hash
# Create customized index view class that handles login & registration

@app.route('/')
def base():
    return render_template("base.html")
@app.route('/admin')
def admin():
    return render_template('/admin/index.html',current_user=current_user)
@app.route('/smartplug', methods=['GET','POST'])
def smartplug():
    return render_template("plug.html")

#Register Route
@app.route('/register', methods=['GET','POST'])
def register():
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        # Get Information
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n",username,password,email)
        # Create an instance of User
        user = User(username,email,password)
        # Open and insert into database
        db.session.add(user)
        # Save info into database
        db.session.commit()
    return render_template('register.html',form = form)

#Login
@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            return redirect(url_for('base'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html',form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('base'))
