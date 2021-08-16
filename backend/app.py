
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
      #user will need to be name pulled from  db
      user = request.args.get('email')
      return render_template('login.html')
   else:
      user = request.form['email']
      return render_template('user.html', username= user)


@app.route('/signup',methods = ['POST', 'GET'])
def signup():
   if request.method == 'GET':
      user = request.args.get('name')
      return render_template('signup.html')
   else:
      user = request.form['fname']
      return render_template('user.html', username= user)
      

@app.route('/user', methods = ['POST', 'GET'])
def showProfile():
   if request.method == 'GET':
      return render_template('user.html')
   else:
      pass

@app.route('/order', methods = ['POST', 'GET'])
def orderFood():
   if request.method == 'GET':
      return render_template('order.html')
   else:
      pass
      

     
if __name__ == '__main__':
   app.run(debug = True)