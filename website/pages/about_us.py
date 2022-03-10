from .. import db
import json
import logging
from flask import redirect, url_for, Blueprint, render_template

about_us_page = Blueprint('about_us', __name__)

@about_us_page.route('/about_us')
def about_us():
    logging.info('user is on about_us page')
    return render_template('About_us.html')