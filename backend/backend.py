
from flask import Flask, redirect, url_for, request , render_template
app = Flask(__name__)
  
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
  
@app.route('/login',methods = ['POST', 'GET'])
def login():
   #return render_template('login.html')

   if request.method == 'GET':
      user = request.args.get('nm')
      return render_template('login.html')
   else:
      user = request.form['nm']
      return redirect(url_for('success',name = user))
          
      
@app.route('/') 
def homePage():
    return (
        render_template('index.html')
    )

@app.route('/menu') 
def getMenu():
    return (
        render_template('menu.html')
    )


@app.route('/order')
def orderFood():
   return render_template('order.html')

     
if __name__ == '__main__':
   app.run(debug = True)