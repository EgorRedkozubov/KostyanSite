from .. import db
import logging
from flask import redirect, url_for, Blueprint, render_template, request, Response, jsonify
from ..models import Order


send_order = Blueprint('order', __name__)

@send_order.route('/send_order')
def add_order():
    content_type=request.headers.get('Content-Type')
    if (content_type!='application/json'):
        return jsonify({'message': 'Content-Type not supported!'})
    json = request.json
    email = json['email']
    phone = json['phone']
    person_name=json['person_name']
    add_new_order=Order(email=email, phone=phone, person_name=person_name)
    try:
        db.session.add(add_new_order)
        db.session.commit()
        res = jsonify({'message': 'Order received successfully!', 'order':json})
        return (res, 201)
    except AttributeError:
        return Response('Error', 499)