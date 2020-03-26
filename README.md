# Recipe website

Milestone Project 3: Data Centric Development - Code Institute

This is a website to allow users to store and access cooking recipes. They are able to view, add, edit and delete recipes. 

This website helps me to show the skills that I have learn to build a Flask website using MongoDB. 

## Demo

A live demo can be found [here](http://flask-recipe-website.herokuapp.com/get_recipes).

## UX
**The primary target audiences are people who want to store their cooking recipe and easily access to them. They also have the possibility to look for inspiration and ideas when they don't know what to cook.**

#### User Stories:

- As a user, I want to view all the recipes stored to be able to choose what I am going to cook.
- As a user, I want to see the description/step by step action of a specific recipe to make sure I succeed.
- As a user, I want to see the ingredients needed for the recipe to make sure I have all ingredients or buy them. 
- As a user, I want to add a new recipe to store my favorite meal or register one that I never tried yet.
- As a user, I want to edit a specific recipe to improve my recipe.
- As a user, I want to search a recipe by recipe name to find it easily.
- As a user, I want to delete a specific recipe because I do not want to use it anymore.

#### This project is the best way to achieve these things because:

- This website is easy to navigate.
- There is no overloading information.
- All the functionnality can be done easily.
- It works well on every device.
- All the links redirect the user to the correct page.
- The "add recipe" form allows users to create a recipe and it can be found on the home page.
- The "edit recipe" form allows users to edit the recipe selected.

#### Wireframes
No wireframes has been used because I decided to use the framework from materializecss.

## Features

**All pages**

- Each page has a responsive **navbar**.
- Each page is responsive. 

**Home page**
The home page allows users to see all the recipes that have been stored in the database. Each recipe can be clicked to view it in details. 

**Add recipe page**
This page allows the users to create a cooking recipe and store it in the database. Then, the recipe will be shown to the home page.

**Recipe description page**
This page shows the description of the recipe selected in the home page. Users are able to edit the recipe or delete it.

**Search page**
The search page allows users to search for a recipe by filling the form using the recipe name they are looking for.

**Recipe found page**
This page shows to the users the recipes that have been found that are matching with their request. It can be one recipe or multiple recipes. You can try to search for beef to see multiple recipes on the page. 

**Type page**
This page allows users to create new types or delete existing types. Type is an additionnal information in the recipe. 

### Features Left to Implement
- In the home page and recipe found page, I would like to add pagination if the recipe list grow. 
- I would like to add a login authentication and register feature.
- I would like to limit the "delete" and "edit" button option for users to only enable them to delete or edit recipes that they have created themselves and not the others. 
- I would like to allow user to search by recipe type and show recipes from that type. This will benefit for people that do not know what to cook and that are looking for inspiration.

## Technologies Used

- **HTML5**
- **CSS3**
- [Materializecss](https://materializecss.com/) it is a front end framework
- [Material.io](https://material.io/) used for the icon
- **Python** - Programming Language used for the backend of the application
- **PyMongo**
- **Flask** - a web framework
- **MongoDB** - Non-relational database to store information
- **Javascript libraries**
    - [JQuery](https://jquery.com) used to simplify DOM manipulation.
- **IDE** used to develop the website: writting, debugging and running the code.
  - [Visual Studio Code](https://code.visualstudio.com/)

## Testing
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and [W3C Markup Validation Service](https://validator.w3.org/) has been used to check the validity of the website code.
- [pep8online](http://pep8online.com/) - check the validity of the Python code. 

### All pages
- The website is fully responsive and behave as expected. Used Chrome DevTools to check all the devices.

- The logo (in the navbar) always leads back the user to the Home page.

- Every link in the navbar redirect the user to the appropriate page.

### Home page
- Check if the recipes load correctly.
- Check if the image of the recipe loads correctly in the good size. 
- Make sure than the default image is shown if no recipe image has been provided when creating the recipe. 
- Check that the view button redirect the user to the correct page. 

### Add recipe page
- Add recipe form: 
    1. Try to submit the empty form and verify that an error message about the required fields appears.
    2. Can not enter negative number for servings, preparation time and cooking time. 
    3. Try to submit the form with all valid input except **Recipe type**  and verify that there an error message appears.
    4. Try to submit the form with one empty field which is required and verify that the error message appears.
    5. Try to submit the form with all valid inputs and verify that successful message appears.

### Recipe description page
- Check if the image of the recipe loads correctly in the good size. 
- Make sure than the default image is shown if no recipe image has been provided when creating the recipe.
- Check if all the information from mongo is showing correctly. 
- Check if the edit button redirect the user to the correct page. 
- Check if the delete button delete the recipe correctly. 

### Edit recipe page
- Edit recipe form: 
    1. Make sure that all the value from mongo fill the fields.
    2. Try to submit the empty form and verify that an error message about the required fields appears.
    3. Can not enter negative number for servings, preparation time and cooking time. 
    4. Try to submit the form with one empty field which is required and verify that the error message appears.
    5. Try to submit the form with all valid inputs and verify that the recipe is edited.

### Type page
- Check if the type data is showned correctly.
- Check if the delete button delete correctly the type. 
- Check if the add type button redirect the user to the correct page. 

### Add type page
- Make sure that the form do not send empty value to the database.
- Check that the data send the type to the database and redirect user to the type page.

### Search recipe page
- Make sure that the form do not send empty value to the database.
- Check that when the recipe is found it redirect the user to the recipe found page. 

### Recipe found page
- Check that the recipes found are showing correctly in the same format that the home page.

### Issue found
In the "add recipe" form and "edit recipe" form the required attribute of the "recipe type" is not working due to the select tag with materialize. It prevented me to show an error message when the recipe type was not selected. The select option tag was hidden and replaced by a unlisted list. Then in my custom javascript file, I had to change the target from select tag to unlisted list tag - Found this workaround with tutor. 

## Deployment
- Project was deployed to heroku. 
- Created Procfile and requirements.txt.
- Set environment variables:
    - IP = 0.0.0.0
    - PORT = 5000
    - MYMONGO_URI = mongodb+srv://<username>:<password>@<cluster_name>-qg4aq.mongodb.net/test?retryWrites=true&w=majority
    
- The code is also hosted on GitHub pages, deployed directly from the master branch.

**To copy the code, you can clone it by following these steps:**

1. On GitHub, navigate to the main page of the repository.
2. Under the repository name, click **Clone or download**.
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. Open the terminal.
5. Type `git clone`, and then paste the URL you copied in Step 3.
``` console
$ git clone https://github.com/USERNAME/REPOSITORY
```
6.Press **Enter**. Your local clone will be created.

To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.

## Credits

### Content
- Recipes from the database where taken from these websites:
    - Beef bourguignon [bbc.co.uk](https://www.bbc.co.uk/food/recipes/boeuf_bourguignon_25475).
    - Burger [spunout.ie](https://spunout.ie/health/article/rp-how-to-make-burgers).
    - Lasagne [spunout.ie](https://spunout.ie/health/article/rp-how-to-make-lasagne).
    - Mongolian beef [dinnerthendessert.com](ttps://dinnerthendessert.com/mongolian-beef/)

### Media
- All recipe images were taken from google images.

### Acknowledgements
I received inspiration for this project by:
    - a previous project that I did during the course: https://task-manager-flask-mongo130.herokuapp.com/get_tasks
    - Multiple cooking website: https://spunout.ie/health/article/rp-how-to-make-burgers // https://www.campbells.com/kitchen/categories/