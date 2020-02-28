import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

# Import the env.py file where I used it for set up the environment variable for my local workspace 
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MYDATABASE')
app.config["MONGO_URI"] = os.environ.get('MYMONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', recipes= mongo.db.recipes.find())

""" Add recipe form """
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', servings = mongo.db.servings.find().sort('serving_number', 1))

if __name__ == '__main__':
    # This app.run is for heroku
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
    # This app.run is for local vscode
    # app.run(debug=True)