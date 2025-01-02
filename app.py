from flask import Flask,render_template,request,redirect,session
from db import database
dbo=database()

app=Flask(__name__)
app.secret_key = "your_secret_key"  # Required to use sessions  

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/perform_register',methods=['post'])
def perfom_register():
    name=request.form.get('user_name')
    email=request.form.get('user_email')
    password=request.form.get('user_password')

    result=dbo.inser_data(name,email,password)
     
    if result==1:
        return render_template('login.html',message='Registration successful now login to proceed')
    else:
        return  render_template('registration.html',message='E-mail already exists')

@app.route('/perform_login',methods=['post'])
def perform_login():
    email=request.form.get('user_email')
    password=request.form.get('user_password')    

    result=dbo.search(email,password)

    if result:
        session['logged_in']=1
        return redirect('/profile')
    else:
        return render_template('login.html',message="incorrect email/pass")
    
@app.route('/profile')
def profile():
    if session['logged_in']==1:
        return render_template('profile.html')
    else:
        return redirect('/')

app.run(debug=True)