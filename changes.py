@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'GET':
      #load page
      return render_template('login.html')
   else:
      email = request.form['email']
      pw = request.form['password']
      
      dbuser = appSystem.loadDBUserByEmail(engine, email)
      print(dbuser)

      if dbuser.email == email and dbuser.password == pw :
         return redirect('user')
         #redirect('user/' + dbuser.email)
      else: 
         return 'failure to login'