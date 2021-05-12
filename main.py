from flask import Flask, render_template, request, redirect, session, flash
import os
import db
app = Flask(__name__)

# https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask/34903502
app.secret_key = os.urandom(24)


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
    db.cursor.execute(f'''Select * FROM `users` WHERE `email` LIKE '{email}' AND `password` LIKE '{password}';''')
    users = db.cursor.fetchall()
    if len(users) > 0:
        session['user_id'] = users[0][0]
        return redirect("/home")
    else:
        return redirect("/")
        

        

#add a new user
@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    db.cursor.execute(f'''INSERT INTO `users`(`user_id`, `name`, `email`, `password`) VALUES (NULL, '{name}', '{email}', '{password}');''')
    db.connection.commit()

    db.cursor.execute(f'''SELECT * FROM `users` WHERE `email` LIKE '{email}';''')
    new_user = db.cursor.fetchall()
    session['user_id'] = new_user[0][0]
    return redirect('/home')
    
if __name__ == '__main__':
    db.createDB()
    app.run(debug=True)

