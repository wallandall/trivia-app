import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
        Set up CORS. Allow '*' for origins.
      '''

    CORS(app, resources={r'*': {'origins': '*'}})

    '''
       The after_request decorator sets Access-Control-Allow
      '''

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

    '''
      Endpoint to handle GET requests
      for all available categories.
    '''

    @app.route('/categories', methods=['GET'])
    def get_categories():
        try:
            categories = Category.query.all()
            if (len(categories) == 0):
                abort(404)

            formatted_categories = {
                category.id: category.type for category in categories}

            return jsonify({
                'success': True,
                'categories': formatted_categories,
                'total_categories': len(Category.query.all())
            })

        except Exception:
            abort(422)

    '''
      Endpoint to handle GET requests
      for all available questions.
    '''
    @app.route('/questions', methods=['GET'])
    def get_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate(request, selection)

        categories = Category.query.order_by(Category.type).all()

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(selection),
            'categories': {category.id: category.type for category in categories},
            'current_category': None
        })
    '''
      Endpoint to delete questions using the ID
    '''
    @app.route('/questions/<question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.get(question_id)
            question.delete()
            return jsonify({
                'success': True,
                'deleted': question_id
            })
        except:
            abort(422)

    '''
      Endpoint to create a new questions and return the question ID
    '''
    @app.route("/questions", methods=['POST'])
    def add_question():
        body = request.get_json()

        new_question = body.get('question')
        new_answer = body.get('answer')
        new_difficulty = body.get('difficulty')
        new_category = body.get('category')
        if (new_question == '' or new_answer == ''):
            abort(400)

        try:
            question = Question(question=new_question, answer=new_answer,
                                difficulty=new_difficulty, category=new_category)
            question.insert()

            return jsonify({
                'success': True,
                'created': question.id,
            })

        except:
            abort(422)

    '''
      Endpoint to search for a question
    '''
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        body = request.get_json()
        search_term = body.get('searchTerm', None)

        if search_term:
            search_results = Question.query.filter(
                Question.question.ilike(f'%{search_term}%')).all()

            return jsonify({
                'success': True,
                'questions': [question.format() for question in search_results],
                'total_questions': len(search_results),
                'current_category': None
            })
        abort(404)

    '''
      Endpoint to Get question based on category ID
    '''
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_question_by_category_id(category_id):

        try:
            questions = Question.query.filter(
                Question.category == str(category_id)).all()

            return jsonify({
                'success': True,
                'questions': [question.format() for question in questions],
                'total_questions': len(questions),
                'current_category': category_id
            })
        except:
            abort(404)

    '''
      Endpoint to Post to get questions to play quiz
    '''
    @app.route('/quizzes', methods=['POST'])
    def play_quiz():

        try:

            body = request.get_json()
            category = body.get('quiz_category')
            previous_questions = body.get('previous_questions')

            if not ('quiz_category' in body and 'previous_questions' in body):
                abort(422)

            if category['type'] == 'click':
                available_questions = Question.query.filter(
                    Question.id.notin_((previous_questions))).all()
            else:
                available_questions = Question.query.filter_by(
                    category=category['id']).filter(Question.id.notin_((previous_questions))).all()

            new_question = available_questions[random.randrange(
                0, len(available_questions))].format() if len(available_questions) > 0 else None

            return jsonify({
                'success': True,
                'question': new_question
            })
        except:
            abort(422)

    '''
      Error Handling
        Not found     :  404
        Unprocessable :  422
        Bad request   :  400
    '''
    @ app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @ app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @ app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    return app
