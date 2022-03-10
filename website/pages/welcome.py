from .. import db
import json
import logging
from flask import redirect, url_for, Blueprint, render_template

welcome_page = Blueprint('welcome', __name__)

@welcome_page.route('/welcome')
def welcome():
    logging.info('user is on welcome page')
    return render_template('Welcome.html')

@welcome_page.route('/')
def default():
    logging.info('user was redirected to welcome page')
    return redirect(url_for('welcome.welcome'))
