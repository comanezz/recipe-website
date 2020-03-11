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

# Add recipe form
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', servings = mongo.db.servings.find(), type = mongo.db.recipe_type.find().sort('type_name', 1))

# Insert recipe to Mongo Database
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

# Recipe description the recipe selected
@app.route('/recipe/<recipe_id>')
def recipe_description(recipe_id):
    one_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('recipedescription.html', recipe = one_recipe)

# Edit the recipe
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_type = mongo.db.recipe_type.find().sort('type_name', 1)
    all_servings = mongo.db.servings.find()
    return render_template('editrecipe.html', recipe = the_recipe, type = all_type, servings = all_servings)

# Update the recipe
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes
    recipe.update({'_id': ObjectId(recipe_id)},
    {
        'author_name': request.form.get('author_name'),
        'serving_number': request.form.get('serving_number'),
        'recipe_name': request.form.get('recipe_name'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_type': request.form.get('recipe_type'),
        'preparation_time': request.form.get('preparation_time'),
        'cooking_time': request.form.get('cooking_time'),
        'ingredients': request.form.get('ingredients'),
        'methods': request.form.get('methods')
    })
    return redirect(url_for('get_recipes'))

# Delete the recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipe = mongo.db.recipes
    recipe.delete_one({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

# --------------- Type ----------------

# Add recipe type
@app.route('/get_type')
def get_type():
    return render_template('type.html', type = mongo.db.recipe_type.find())

# Delete recipe type
@app.route('/delete_type/<type_id>')
def delete_type(type_id):
    recipe_type = mongo.db.recipe_type
    recipe_type.delete_one({'_id': ObjectId(type_id)})
    return redirect(url_for('get_type'))
    

if __name__ == '__main__':
    # This app.run is for heroku
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
    # This app.run is for local vscode
    # app.run(debug=True)