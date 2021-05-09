from flask import Flask, render_template, request,session, redirect
import os
import db

app = Flask(__name__)

with open(".pw") as f:
  password = f.read()

app = Flask(__name__, static_url_path='/static', static_folder='static/')
# https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask/34903502
app.SECRET_KEY = os.urandom(24)


#base page
@app.route('/')
def signin():
    return render_template("signin.html")

#user signup
@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/signout')
def signout():
    session.pop('user_id')
    return red

#user signed in
@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template ("home.html")
    else:
        return redirect("/")

#to validate user login
@app.route('/validation', methods=['POST'])
def validation():
    email = request.form.get('email')
    password = request.form.get('password')
    db.cursor.execute(f"""Select * FROM users WHERE email LIKE '{email}' AND password LIKE '{password}'""")
    users = cursor.fetchall()
    if len(users) > 0:
        session['user_id'] = users[0][0]
        return redirect("home.html")
    else:
        return redirect("login.html")

#add a new user

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    s = f'''INSERT INTO students(id, name, email, password) VALUES (NULL, '{user_name}', '{user_email}', '{user_password}';'''
    db.cursor.execute(s)
    db.cursor.connection.commit()
    new_user = db.cursor.fetchall()
    session['user_id'] = new_user[0][0]
    return redirect('/home')

if __name__ == '__main__':
    db.createDB()
    app.run(host='0.0.0.0', port='8080',ssl_context=('cert.pem', 'privkey.pem'))
    
