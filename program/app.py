from user import User 
from food import Pizzas , Pastas , Salads , Beverages
from order import Order
from menu import Menu
from system import System
from dbclass import SaveUsers

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload

from flask import Flask, redirect, url_for, request , render_template
app = Flask(__name__)

appSystem  = System()
appSystem.createNewUser("Admin", "Admin", "8009993333", "admin@google.com", "admin")

Marios = Menu()
Marios.addPasta("Pesto" , 12.99, "basic" , "pesto")
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
      empty = ""
      if (email != empty or pw != empty):
         user = appSystem.findUserByEmailAndPW(email, pw)

         Session = sessionmaker(bind=engine)
         session = Session()
         user_by_email = session.query(SaveUsers).filter(SaveUsers.email==email).first()
         print(user_by_email)



         if user == None :
            return 'failure to login'
         else:
            return redirect('user/' + user.email)
            # return  render_template('user.html', username= user.fname )
      else: 
         return 'failure to login'

@app.route('/user/<user>')
def profile(user):
   if request.method == 'GET':
      thisuser = appSystem.findUserByEmail(user)
      return render_template('user.html', username = thisuser.fname, email= thisuser.email , phone = thisuser.phonenum)
   else:
      redirect('user/'+ user +"/order")


# @app.route('/user', methods = ['POST', 'GET'])
# def showProfile(user):
#    if request.method == 'GET':
#       thisuser = appSystem.findUserByEmail(user)
#       return render_template('user.html', username = thisuser.fname, email= thisuser.email , phone = thisuser.phonenum)
#    else:
#       return redirect('order')



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
     
         Session = sessionmaker(bind=engine)
         session = Session()
         newUser =  SaveUsers(fname=fname, lname=lname, phone=phone, email=email, password=pw)
         session.add(newUser)
         session.commit()

         
         return render_template('user.html', username= fname)
      



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


