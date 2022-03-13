from flask import Blueprint, make_response, request, Response, jsonify
import random


cookies = Blueprint('cookies', __name__)

@cookies.route('/setup_user_id_cookie')
def setup_user_id_cookie():
    if not request.cookies.get('user_key'):
        user_key = 'something'
        res = jsonify({'message': 'User key was setup successfully', 'user':{'user_key': user_key}})
        res.set_cookie('user_key', user_key, max_age=60 * 60 * 24 * 365 * 2)
    else:
        user_key = request.cookies.get('user_key')
        res = jsonify({'message': 'User already had user_key', 'user':{'user_key': user_key}})
    return res



