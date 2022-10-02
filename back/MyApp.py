import json
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

# model
class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200)) 
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin
# model

# views
@app.route('/')
def show_all():
    res=[]
    for student in students.query.all():
        res.append({"addr":student.addr,"city":student.city,"id":student.id,"name":student.name,"pin":student.pin})
    return  (json.dumps(res))
   

@app.route('/new', methods = ['GET', 'POST'])
def new():
    request_data = request.get_json()
    # print(request_data['city'])
    city = request_data['city']
    name= request_data["name"]
    addr= request_data["addr"]
    pin= request_data["pin"]

    newStudent= students(name,city,addr,pin)
    db.session.add (newStudent)
    db.session.commit()
    return "a new rcord was create"

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)



class Category(db.Model):
    id = db.Column('category_id', db.Integer, primary_key = True)
    cat = db.Column(db.String(100))


    def __init__(self,cat):
        self.cat=cat
# model

class Products(db.Model):
    id = db.Column('product_id', db.Integer, primary_key = True)
    prod_name = db.Column(db.String(100))
    price = db.Column(db.integer(50))
    prod_cat=db.Column(db.String(100), db.ForeignKey('category.id'))

    def __init__(self,prod_name,price,prod_cat=0 ):
        self.prod_name = prod_name
        self.price = price
        self.prod_cat = prod_cat
       
# model
@app.route('/cats')
def show_all_cats():
    res=[]
    for cat in Category.query.all():
        res.append({"cat":cat.cat,"id":cat.id})
    return  (json.dumps(res))


@app.route('/prod')
def show_all_prods():
    res=[]
    for prod in Products.query.all():
        res.append({"id":prod.id,"prod_name":prod.prod_name ,"price":prod.price ,"prod_cat":prod.prod_cat})
    return  (json.dumps(res))
