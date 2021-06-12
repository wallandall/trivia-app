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





