from flask import Flask, render_template, request, redirect, session, flash
import os
import db
app = Flask(__name__)

# https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask/34903502
app.SECRET_KEY = os.urandom(24)


#base page
@app.route("/")
def signin():
    return render_template("signin.html")

#signup page
@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/logout")
def signout():
    session.pop('user_id')
    return redirect("/")

#user signed in
@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template("home.html")
    else:
        return redirect("/")

#to validate user login
@app.route("/validation", methods=["POST"])
def validation():
    email = request.form.get('email')
    password = request.form.get('password')
    db.cursor.execute(f"""Select * FROM `users` WHERE `email` LIKE '{email}' AND `password` LIKE '{password}';""")
    users = db.cursor.fetchall()
    if len(users) > 0:
        session['user_id'] = users[0][0]
        return redirect("/home")
    else:
        return redirect("/")
        flash("Invalid Email or Password", category="error")

#add a new user
@app.route('/add', methods=['POST'])
def add():
    #below block taken from moodle "Setup and example server"
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    s = f'''INSERT INTO users(id, name, email, password) VALUES (NULL, '{name}', '{email}', '{password}');'''
    db.cursor.execute(s)
    db.cursor.connection.commit()

    new_user = db.cursor.fetchall()
    session['user_id'] = new_user[0][0]
    return redirect('/home')
    
if __name__ == '__main__':
    db.createDB()
    app.run(debug=True)

