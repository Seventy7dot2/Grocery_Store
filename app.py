from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)
app.secret_key = 'super-secret-key'
with open('config.json', 'r') as c:
    params = json.load(c)["params"]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grocerystore.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    unit = db.Column(db.String(5), nullable=False)
@app.route("/")
def login():
    return render_template('index.html')
@app.route("/home")
def home():
    products = Product.query.filter_by().all
    return render_template('home.html', products=products)
@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():

    if ('user' in session and session['user'] == params['admin_user']):
        return 'Logged in <a href="/logout">  <button class="btn btn-primary"> Logout</button></a>'


    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == params['admin_user'] and userpass == params['admin_password']):
            #set the session variable
            session['user'] = username
            return 'Logged in <a href="/logout">  <button class="btn btn-primary"> Logout</button></a>'

    return render_template('login.html', params=params)
@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/')
app.run(debug='true')