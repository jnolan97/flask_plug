from venv import app
from flask import render_template, request, redirect, url_for

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/login', methods = ['GET','POST'])
def login():
    return redirect(url_for('base'))

@app.route('/smartplug', methods=['GET','POST'])
def smartplug():
    return render_template("plug.html")
