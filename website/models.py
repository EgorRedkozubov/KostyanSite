from . import db
from sqlalchemy.sql import func


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(10000))
    price = db.Column(db.Integer)
    isAvailable = db.Column(db.Boolean, default=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    phone = db.Column(db.String(20))
    person_name = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())


class ProductsInOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    Order_id = db.Column(db.Integer)
