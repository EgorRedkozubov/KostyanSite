from .. import db
import json
import logging
from flask import redirect, url_for, Blueprint, render_template, request, jsonify, Response
from ..models import Products
import random

products_page = Blueprint('products', __name__)


@products_page.route('/products')
def products():
    page = request.args.get('id', default=None, type=int)
    try:
        data = Products.query.filter_by(id=page).first()
        product = {"name": data.name, "description": data.description, "price": data.price,
                   "isAvailable": data.isAvailable}
        return product
    except AttributeError:
        return Response("Product with that id not exists.", 400)


@products_page.route('/add_product', methods=['POST'])
def add_product_to_basket():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return jsonify({'message': 'Content-Type not supported!'})
    json = request.json
    name = json["name"]
    description = json["description"]
    price = json["price"]
    isAvailable = json["isAvailable"]
    new_product = Products(name=name, description=description, price=price, isAvailable=isAvailable)
    try:
        db.session.add(new_product)
        db.session.commit()
        res = jsonify({'message': f'product "{name}" added successfully',
                       'product': json})
        return (res, 201)
    except AttributeError:
        return {'message':'Error'}, 499


@products_page.route('/delete_product', methods=['DELETE'])
def delete_product_from_basket():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return 'Content-Type not supported!'
    json = request.json
    product = json['product']

    return jsonify({'message':f'{product} was deleted successfully!', 'product':{json}}), 209
