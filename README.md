# Recipe App

#### A recipe application that helps to track the steps and ingredients in making a particular recipe


### Technologies used
- Pyhton django
- Django Rest Framework

#### Installation
Follow the following steps to setup the project

**Clone the Repo**
`https://github.com/el-Joft/Recipe-app.git`

#### Navigate to the project directory
`cd recipe-app`

#### Create a virtual environment by running

`virtualenv recipe-app-env`

##### Activate the environment

`source recipe-app-env/bin/activate`

#### Running and Development

##### Install dependencies

`pip install -r requirements.txt`

##### Start the application

`python manage.py runserver`

##### Try out the endpoint with your favourite API testing tool
- create a user - POST http://127.0.0.1:8000/api/v1/create_user/
- create an Ingredient - POST  http://127.0.0.1:8000/api/v1/ingredients/
- create a recipe - POST http://127.0.0.1:8000/api/v1/recipe/
- list all recipe - GET http://127.0.0.1:8000/api/v1/recipe/
- list single recipe - GET http://127.0.0.1:8000/api/v1/recipe/id
- get recipe created by a user GET http://127.0.0.1:8000/api/v1/recipe/user/userid
- update a recipe - PATCH http://127.0.0.1:8000/api/v1/recipe/id
- delete a recipe - DELETE http://127.0.0.1:8000/api/v1/recipe/id

#### Todo
- [ ]    User Authentication (jwt token generation)
- [ ]   RUD operation on Ingredients and Steps
- [ ]   host application on heroku


#### Author: Timothy Omotayo




