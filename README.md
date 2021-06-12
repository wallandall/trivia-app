# Full Stack API


## Full Stack Trivia
Full Statck Trivia, is an application that allows users to play the trivia game. The application consists of a React Frontend and a Flask API Backend. The application allows the following actions:

1. Display questions by all questions and questions based on category. Users can see the rating, dificulty and togle the answers for each question.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

## Setup

The application consists of a React front end a Flask backend which uses a Postgresql Databse. Follow the below steps to setup a local development environemnt
### Backend Setup
1. For this project we use the Postgresql databse, if a database is not available a test database can be setup using this [Docker Image](https://github.com/wallandall/postgres)
   1. Setup the trivia database using the below commands:
   
   ```psql -U postgres trivia < trivia.psql```

2. From your project directory initialize and activate a virtualenv using: 
   
   ``` python -m virtualenv venv ```
   
   ```source env/bin/activate ```

>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
    ``` source env/Scripts/activate ```

3. Install the dependencies from the backen directory:
   
    ``` pip install -r requirements.txt ```

4. Run the development server from the backend folder:
   
   ``` export FLASK_APP=flaskr ``` 

   ``` export FLASK_ENV=development ```

   ``` flask run ```
   
   >**Note** - for Windows CMD:
    ``` set FLASK_APP=flaskr ``` 

   ``` set FLASK_ENV=development```
   
   ``` flask run ```

    >**Note** - for Windows PowerShell:
    ``` $env:FLASK_APP = "flaskr" `` 

   ``` $env:FLASK_ENV = "development" ```
   
   ``` flask run ```






#######################################################
#######################################################

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository](https://github.com/wallandall/trivia-app.git) and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. 

### Backend
The [./backend](https://github.com/udacity/FSND/blob/master/projects/02_trivia_api/starter/backend/README.md) directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in `__init__.py` to define your endpoints and can reference models.py for DB and SQLAlchemy setup. These are the files you'd want to edit in the backend:

1. *./backend/flaskr/`__init__.py`*
2. *./backend/test_flaskr.py*


### Frontend

The [./frontend](https://github.com/udacity/FSND/blob/master/projects/02_trivia_api/starter/frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

1. What are the end points and HTTP methods the frontend is expecting to consume?
2. How are the requests from the frontend formatted? Are they expecting certain parameters or payloads? 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with `TODO`. These are the files you'd want to edit in the frontend:

1. *./frontend/src/components/QuestionView.js*
2. *./frontend/src/components/FormView.js*
3. *./frontend/src/components/QuizView.js*


By making notes ahead of time, you will practice the core skill of being able to read and understand code and will have a simple plan to follow to build out the endpoints of your backend API. 



>View the [README within ./frontend for more details.](./frontend/README.md)
