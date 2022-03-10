from .. import db
import json
import logging
from flask import redirect, url_for, Blueprint, render_template, request
from ..models import Products
import random

products_page = Blueprint('products', __name__)

@products_page.route('/products')
def products():
    return render_template('Products.html')

@products_page.route('/add_product', methods=['POST'])
def add_product_to_basket():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return 'Content-Type not supported!'
    json = request.json
    name = json["name"]
    description = json["description"]
    price = json["price"]
    isAvailable=json["isAvailable"]
    new_product = Products(name=name, description=description, price=price, isAvailable=isAvailable)
    try:
        db.session.add(new_product)
        db.session.commit()
        logging.info(f'product{name} added successfully')
        return 'ok', 200
    except AttributeError:
        return 400


@products_page.route('/delete_product', methods=['DELETE'])
def delete_product_from_basket():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return 'Content-Type not supported!'
    json = request.json
    product=json['product']


    return 0
