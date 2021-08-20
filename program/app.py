from user import User 
from food import Pizzas , Pastas , Salads , Beverages
from order import Order
from menu import Menu
from system import System
from dbclass import DBUsers

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload

from flask import Flask, redirect, url_for, request , render_template
app = Flask(__name__)

appSystem  = System()

Marios = Menu()

Marios.addPizza("Pepperoni", 15.99)
Marios.addPizza("Cheese", 12.99)
Marios.addPizza("Meat Lovers", 17.99)
Marios.addPizza("Pesto", 14.99)
Marios.addPizza("Hawaiian", 16.99)
Marios.addPizza("Vegetarian", 15.99)


Marios.addPasta("Pesto" , 12.99, "basic" , "Pesto")
Marios.addPasta("Chicken Alfredo" , 12.99, "basic" , "Alfredo")
Marios.addPasta("Shrimp Alfredo" , 12.99, "basic" , "Alfredo")
Marios.addPasta("Lasagna" , 12.99, "basic" , "Marianara")
Marios.addPasta("Scampi" , 12.99, "basic" , "White")


Marios.addBeverage("Coke", 1.99)
Marios.addBeverage("Sprite", 1.99)


#engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///./newdb.db', echo=True)
Base = declarative_base()
Base.metadata.create_all(engine) 


@app.route('/') 
def landingPage():
    return (
        render_template('index.html')
    )

@app.route('/home') 
def homePage():
    return (
        render_template('index.html')
    )

#display our menu
@app.route('/menu') 
def getMenu():
   return (
        render_template('menu.html',content =Marios.menu_items)
    )


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
  
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'GET':
      #load page
      return render_template('login.html')
   else:
      email = request.form['email']
      pw = request.form['password']      
      dbuser = appSystem.loadDBUserByEmail(engine, email)

      if dbuser.email == email and dbuser.password == pw :
         return redirect('user')
      elif dbuser == None:
         return 'User cannot be found'
      else: 
         return 'failure to login'


# @app.route('/user/<user>')
# def profile(user):
#    if request.method == 'GET':
#       currentuser = appSystem.findUserByEmail(user)
#       return render_template('user.html', username = currentuser.fname, email= currentuser.email , phone = currentuser.phonenum)
#    else:
#       redirect('order')


@app.route('/user', methods = ['POST', 'GET'])
def showProfile():
   if request.method == 'GET':
      currentuser = appSystem.currentUser
      if currentuser == None :
         return redirect('login')
      else:
         return render_template('user.html', username = currentuser.fname, email= currentuser.email , phone = currentuser.phone)
   
   #post Request
   else:
          
      
      return redirect('order')



@app.route('/signup',methods = ['POST', 'GET'])
def signup():
   if request.method == 'GET':
    
      return render_template('signup.html')
   else:   
      fname = request.form['fname']
      lname = request.form['lname']
      phone = request.form['phone']
      email = request.form['email']
      pw = request.form['password']
      form_data = request.form

      if (fname == '' or lname == '' or phone== '' or email=='' or pw==''):
         return 'Data fields cannot be left empty'

      else:
         appSystem.createNewUser(fname, lname, phone , email, pw)
         appSystem.displayUsers()
         
         current_user= appSystem.currentUser
         current_user.saveToDB(engine)
         
   
         return render_template('user.html', username= current_user.fname , email = current_user.email , phone =  current_user.phone)
      



@app.route('/order', methods = ['POST', 'GET'])
def orderFood():

   print("hello")
   if request.method == 'GET':
      print("loading!")
      return render_template('order.html')

   else:
      print("over here now ")
      test = request.args.to_dict()
      req = request
      print(test , "req: " , req)

      return 'success'


if __name__ == '__main__':
   app.run(debug = True)


