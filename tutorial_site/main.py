import projects #projects definitions are placed in different file
#import data
# Import modules for CGI handling
import cgi, cgitb
from transfer import encode
from data import *

# Create instance of FieldStorage
from pip._vendor import requests

from __init__ import restapi_bp
from flask import render_template


# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import os
#create a Flask instance
app = Flask(__name__)





@app.route('/')
def home_route():
    return render_template("home.html", projects=projects.setup())
    #if not session.get('logged_in'):
     #   return render_template('login.html')
    #else:
     #   return render_template("home.html", projects=projects.setup())
@app.route('/test/')
def test_route():
    return render_template("test.html", projects=projects.setup())
#, username=request.form['username'], password=request.form['password']


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template("form.html")
    elif request.method == 'POST':
        if request.form.get('title') != '' and request.form.get('category') != '' and request.form.get('description') != '' :
            title = request.form.get('title')
            category = request.form.get('category')
            description = request.form.get('description')
            return redirect("/showform?title=" + str(title) +"&category=" + str(category) + "&description=" + str(description) + "&video=" + str(video), code=302)
        else:
            return render_template("form.html")

@app.route('/calc/')
def calc_route():
    return render_template("Class.html", projects=projects.setup(), data1=calc)
@app.route('/phys/')
def phys_route():
    return render_template("Class.html", projects=projects.setup(), data1=phys)
@app.route('/euro/')
def euro_route():
    return render_template("Class.html", projects=projects.setup(), data1=euro)
@app.route('/hist/')
def hist_route():
    return render_template("Class.html", projects=projects.setup(), data1=hist)
@app.route('/precalc/')
def precalc_route():
    return render_template("Class.html", projects=projects.setup(), data1=pcalc)
@app.route('/stat/')
def stat_route():
    return render_template("Class.html", projects=projects.setup(), data1=stats)
@app.route('/csip/')
def csip_route():
    return render_template("Class.html", projects=projects.setup(), data1=csip)
@app.route('/eeg/')
def egg_route():
    return render_template("egg.html", projects=projects.setup())

@app.route('/showform', methods=['POST', 'GET'])
def showform():
    title = request.args.get('title')
    category = request.args.get('category')
    description = request.args.get('description')
    return render_template("showform.html", title=title , description=description , category=category)

@app.route('/joke/',  methods=['GET', 'POST'])
def joke():
    # call to random joke web api
    url = 'https://official-joke-api.appspot.com/jokes/programming/random'
    response = requests.get(url)
    # formatting variables from return
    setup = response.json()[0]['setup']
    punchline = response.json()[0]['punchline']
    return render_template("joke.html", setup=setup, punchline=punchline)


if __name__ == "__main__":
    #runs the application on the repl development server
    app.secret_key = os.urandom(12)
    app.run(debug=True)

