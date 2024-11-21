# Title; Final Project - CST205
# Author: Carlos Solian, Aryll Pacheco, Bryson Ruck, & Sarah Wafa


# Adding Them to Git
# git add -A
# Commit
# git commit -m "Something Meaningful"
# Push
# git push -u origin main

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
boostrp = Bootstrap5(app)

@app.route('/')
def homepage():
    return render_template('homepage.html')

# Carlos's Home Page
@app.route('/carlos')
def carlos():
    return render_template('CarlosHomePage.html')