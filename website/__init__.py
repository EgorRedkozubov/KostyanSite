import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from helpers.secret_key import secret_key


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:admin@localhost/{DB_NAME}'
    db.init_app(app)
    logging.info('app was created successfully')

    from .pages.welcome import welcome_page
    from .pages.about_us import about_us_page
    # from .pages.basket import users_basket
    from .pages.products import products_page
    from .pages.order import send_order
    from helpers.set_cookies import cookies

    app.register_blueprint(send_order, url_prefix='/')
    app.register_blueprint(welcome_page, url_prefix='/')
    app.register_blueprint(about_us_page, url_prefix='/')
    # app.register_blueprint(users_basket, url_prefix='/')
    app.register_blueprint(products_page, url_prefix='/')
    app.register_blueprint(cookies,url_prefix='/cookies/')

    from .models import Order, Products

    # create_database(app)
    logging.info('database was established successfully')

    return app

# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')
