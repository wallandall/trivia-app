# Full Stack API


## Full Stack Trivia
Full Statck Trivia, is an application that allows users to play the trivia game. The application consists of a React Frontend and a Flask API Backend. The application allows the following actions:

1. Display questions by all questions and questions based on category. Users can see the rating, dificulty and togle the answers for each question.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

## Setup

The application consists of a React frontend a Flask backend which uses a Postgresql Databse. Follow the below steps to setup a local development environemnt
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

   ``` flask run --reload```
   
   >**Note** - for Windows CMD:

    ``` set FLASK_APP=flaskr ``` 

   ``` set FLASK_ENV=development ```
   
   ``` flask run --reload```

    >**Note** - for Windows PowerShell:

    ``` $env:FLASK_APP = "flaskr" ```  

   ``` $env:FLASK_ENV = "development" ```
   
   ``` flask run --reload ```

### Frontend Setup
From the frontend directory run the below commands:
1. To install dependancies : ```npm install ```
2. To start local server: ``` npm start ```
You can access the frontend by navigating to : ``` http://localhost:3000 ```


## Testing
To run tests run:
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py

```

## API Endpoints

 ``` 
 GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs. 
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true, 
  "total_categories": 6
} 
```
```
GET '/questions?page=${integer}'
- Fetches a paginated set of questions, a total number of questions, all categories and current category string. 
- Request Arguments: page - integer
- Returns: An object with 10 paginated questions, total questions, object including all categories, and current category string
{  
   'categories': { '1' : "Science",
    '2' : "Art",
    '3' : "Geography",
    '4' : "History",
    '5' : "Entertainment",
    '6' : "Sports" },
    'questions': [
        {
            'id': 1,
            'question': 'This is a question',
            'answer': 'This is an answer', 
            'difficulty': 5,
            'category': 2
        },
    ],
    'totalQuestions': 100,
    "success": true,    
    'currentCategory': 'History'
}
```

```
GET '/categories/${id}/questions'
- Fetches questions for a cateogry specified by id request argument 
- Request Arguments: id - integer
- Returns: An object with questions for the specified category, total questions, and current category string 
{
  "current_category": 2, 
  "questions": [
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ], 
  "success": true, 
  "total_questions": 4
}
```

```
DELETE '/questions/${id}'
- Deletes a specified question using the id of the question
- Request Arguments: id - integer
- Returns: Returns Success and Question ID that was deleted. 
```

```
POST '/quizzes'
- Sends a post request in order to get the next question 
- Request Body: 
{'previous_questions':  an array of question id's such as [1, 4, 20, 15]
'quiz_category': a string of the current category }
- Returns: a single new question object 
{
    'question': {
        'id': 1,
        'question': 'This is a question',
        'answer': 'This is an answer', 
        'difficulty': 5,
        'category': 4
    }
}
```

```
POST '/questions'
- Sends a post request in order to add a new question
- Request Body: 
{
    'question':  'Heres a new question string',
    'answer':  'Heres a new answer string',
    'difficulty': 1,
    'category': 3,
}
- Returns: Does not return any new data
```

```
POST '/questions'
- Sends a post request in order to search for a specific question by search term 
- Request Body: 
{
    'searchTerm': 'this is the term the user is looking for'
}
- Returns: any array of questions, a number of totalQuestions that met the search term and the current category string 
{   
   "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
    'questions': [
        {
            'id': 1,
            'question': 'This is a question',
            'answer': 'This is an answer', 
            'difficulty': 5,
            'category': 5
        },
    ],
    "success": true, 
    "total_questions": 30
}
```
