from flask import Flask, render_template, request, session, redirect, url_for, flash
from dbmodel import *
import json
import os
app = Flask(__name__)
app.secret_key = 'super-secret-key'
with open('config.json', 'r') as c:
    params = json.load(c)["params"]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.sqlite3'
db.init_app(app)
app.app_context().push()
app.config['UPLOAD_FOLDER'] = 'static/img'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

@app.route("/")
def login():
    return render_template('index.html')
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        try:
            ud= User.query.filter_by(uname=username,password=userpass).first()
            uid=ud.uname
            uip=ud.password
            if (username == uid and userpass == uip):
                #set the session variable
                global cname
                cname= username
                session['user'] = username
                return redirect('/cview')
        except:
            return render_template('ulogin.html', params=params)
    return render_template('ulogin.html', params=params)
@app.route("/signup",methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        u=User(uname=username,password=userpass)
        db.session.add(u)
        db.session.commit()
        return redirect('/home')
    return render_template('signup.html')
@app.route("/dashboard",methods=['GET', 'POST'])
def dashboard():

    if ('admin' in session and session['admin'] == params['admin_user']):
        products= Product.query.all()
        return redirect("/aview")


    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == params['admin_user'] and userpass == params['admin_password']):
            #set the session variable
            session['admin'] = username
            products= Product.query.all()
            return redirect("/aview")

    return render_template('login.html', params=params)
@app.route("/aview")
def aview():
    if ('admin' in session and session['admin'] == params['admin_user']):
        categories=Category.query.all()
        return render_template('aview.html', categories=categories)
@app.route("/aview/<int:caid>")
def cadview(caid):
    cat= Category.query.get(caid)
    pros= cat.pro
    return render_template('cpview.html', pros=pros, cat=cat)
@app.route("/categories")
def categories():
    categories=Category.query.all()
    return render_template('categories.html', categories=categories)
@app.route("/categories/<int:caid>")
def catpro(caid):
    cat= Category.query.get(caid)
    pros= cat.pro
    return render_template('catpro.html', pros=pros, cat=cat)
@app.route("/additem/<int:cno>",methods=['GET', 'POST'])
def additem(cno):
    if request.method=='POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            pname=request.form.get('name')
            punit=request.form.get('unit')
            pqnt=int(request.form.get('quantity'))
            peach=int(request.form.get('peach'))
            file = request.files['file']
            product=Product(name=pname, unit=punit, quantity=pqnt, cid=cno, peach=peach)
            db.session.add(product)
            db.session.commit()
            filename = f"{product.pid}_{file.filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            product.image_url = url_for('static', filename=f'img/{filename}')
            db.session.commit()
            return redirect("/aview")
    cat= Category.query.get(cno)
    return render_template('additem.html',cat=cat)
@app.route("/changecname/<int:cno>",methods=['GET', 'POST'])
def changecname(cno):
    cat= Category.query.get(cno)
    if request.method=='POST':
        ncname=request.form.get('name')
        cat.name=ncname
        db.session.commit()
        return redirect('/aview')
    return render_template('changename.html',cat=cat)
@app.route("/addcat",methods=['GET', 'POST'])
def addcat():
    if request.method=='POST':
        ncname=request.form.get('name')
        nc=Category(name=ncname)
        db.session.add(nc)
        db.session.commit()
        return redirect('/aview')
    return render_template('addcat.html')
@app.route("/cview")
def cview():
    if ('user' in session and session['user'] == cname):
        
        products= Product.query.all()
        return render_template('home.html', products=products)
    return render_template('index.html')
@app.route("/logout")
def logout():
    try:
        session.pop('admin')
    except:
        session.pop('user')
    finally:
        return redirect('/')
if __name__=="__main__":
    app.run(debug='true')