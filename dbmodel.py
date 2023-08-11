from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Category(db.Model):
    cid = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    pro= db.relationship('Product', backref ="cat")
class Product(db.Model):
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String(200))
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(5), nullable=False)
    peach = db.Column(db.Integer, nullable=False)
    cid = db.Column(db.Integer, db.ForeignKey("category.cid"))
class User(db.Model):
    uname = db.Column(db.String(20), primary_key=True, nullable=False)
    password = db.Column(db.String(30),primary_key=True, nullable=False)
class Order(db.Model):
    oid = db.Column(db.Integer, primary_key=True, nullable=False)
    uname = db.Column(db.String(20), db.ForeignKey("user.uname"))
