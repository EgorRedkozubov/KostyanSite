# from .. import db
# import json
# import logging
# from flask import redirect, url_for, Blueprint, render_template, request
#
#
# users_basket = Blueprint('basket', __name__)
#
# @users_basket.route('/basket')
# def my_basket():
#     return render_template('Basket.html')
#
# @users_basket.route('/change_basket', methods=['POST'])
# def add_product_to_basket(json):
#     content_type = request.headers.get('Content-Type')
#     if (content_type != 'application/json'):
#         return 'Content-Type not supported!'
#     json = request.json
#     product_id=json['product_id']
#     amount=json['amount']
#     add_new_product_to_basket=Basket(amount=amount, product_id=product_id)
#     return 0
