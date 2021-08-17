from src.User import User
from src.Food import Pizzas , Pastas , Salads , Beverages
from src.Order import Order
from src.Menu import Menu

from flask import Flask, redirect, url_for, request , render_template
app = Flask(__name__)
       
      
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


@app.route('/menu') 
def getMenu():
    return (
        render_template('menu.html')
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
      user = request.form['email']
      pw = request.form['password']
      if (user != "" or pw !=  ""):
         return render_template('user.html', username= user)
      else: 
         return 'failure to login'


@app.route('/signup',methods = ['POST', 'GET'])
def signup():
   if request.method == 'GET':
     
      user = request.args.get('name')
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
         return render_template('user.html', username= fname)
      

@app.route('/user', methods = ['POST', 'GET'])
def showProfile():
   if request.method == 'GET':
      return render_template('user.html')
   else:
      pass

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

#some changes    
#fix this please
#did it work?


     
if __name__ == '__main__':
   app.run(debug = True)