from flask import Flask, render_template, request
import mysql.connector
import db
app = Flask(__name__, static_url_path='/static', static_folder='static/')

connection = mysql.connector.connect(host="137.135.135.105", username="azureuser", database="userData")
cursor = connection.cursor()
#base page
@app.route('/')
def signin():
    return render_template("signin.html")

#user signup
@app.route('/signup')
def signup():
    return render_template("signup.html")

#user signed in
@app.route('/home')
def home():
    return render_template("home.html")

#to validate user login
@app.route('/validation', methods=['POST'])
def validation():
    email = request.form.get('email')
    password = request.form.get('password')
    cursor.execute(f"""Select * FROM `users` WHERE `email` LIKE '{email}' AND `password` LIKE '{password}'""")
    users = cursor.fetchall()
    if len(users) > 0:
        return render_template("home.html")
    else:
        return render_template("login.html")

#add a new user
@app.route('/add')
def add():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    cursor.execute(f"""Insert INTO `users` (`user_id`, `name`,`email`,`password`) VALUES (NULL, '{name}', '{email}', '{password}')""")

if __name__ == '__main__':
    db.createDB()
    app.run(host='0.0.0.0', port='80')
    
