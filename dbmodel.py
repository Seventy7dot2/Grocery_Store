from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
class Category(db.Model):
    cid = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    pro= db.relationship('Product', backref ="cat", cascade='all, delete-orphan')
class Product(db.Model):
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String(200))
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(5), nullable=False)
    peach = db.Column(db.Integer, nullable=False)
    cid = db.Column(db.Integer, db.ForeignKey("category.cid"))
    carts = db.relationship('Cart', backref='product', lazy=True)
class User(db.Model):
    uname = db.Column(db.String(20), primary_key=True, nullable=False)
    password = db.Column(db.String(30), primary_key=True, nullable=False)
    carts = db.relationship('Cart', backref='user', lazy=True)
    orders = db.relationship('Order', backref='user_backref', lazy=True)
class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.uname'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.pid'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cart_total = db.Column(db.Float, nullable=False)

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20), db.ForeignKey('user.uname'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    total_order_price = db.Column(db.Float, nullable=False, default=0.0)
    products = db.relationship('Product', secondary='order_products', backref=db.backref('orders', lazy='dynamic'))

class OrderProduct(db.Model):
    __tablename__ = 'order_products'
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.pid'), primary_key=True)