from venv import app
from flask import render_template, request, redirect, url_for

@app.route('/')
def base():
    return render_template("base.html")
