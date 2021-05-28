from flask import Flask, render_template, request, redirect, session, flash
import covid_data
import os
import db
app = Flask(__name__)


#will grant a 24 digit code to a user upon signin
app.secret_key = os.urandom(24) 

#base page
@app.route("/")
def signin():
    return render_template("signin.html")

#signup page
@app.route("/signup")
def signup():
    return render_template("signup.html")

#logout page
@app.route("/logout")
def signout():
    session.pop('user_id')
    return redirect("/")

#if user is in session return home data, else redirect them to base page
@app.route('/home')
def home():
    if 'user_id' in session:
        data = covid_data.world()
        countries_data = covid_data.countries()
        return render_template("home.html", data=data, countries=countries_data)
    else:
        return redirect("/")

#user profile page
@app.route('/profile')
def profile():
    if 'user_id' in session:
        return render_template('profile.html')
    else:
        return redirect("/")

#to validate user login
#upon post, search database for matching email and password
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
        flash("Email or Password is incorrect", category='error')
        return render_template('signin.html', flash=flash)

#add a new user
#upon post, checks if user already exists, if password len is less than 5
#if not then inserts the user into the db and logs them in
@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        name = request.form.get('user_name')
        email = request.form.get('user_email')
        password = request.form.get('user_password')
        db.cursor.execute(f'''SELECT * FROM `users` WHERE `email` LIKE '{email}';''')
        check_email = db.cursor.fetchall()
        if len(check_email) != 0:
            flash("Email already in use", category='error')
            return render_template('signup.html', flash=flash)
        elif len(password) < 5:
            flash("Password must be at least 5 characters long", category='error')
            return render_template('signup.html', flash=flash)
        else:
            db.cursor.execute(f'''INSERT INTO `users`(`user_id`, `name`, `email`, `password`) VALUES (NULL, '{name}', '{email}', '{password}');''')
            db.connection.commit()
            db.cursor.execute(f'''SELECT * FROM `users` WHERE `email` LIKE '{email}';''')
            new_user = db.cursor.fetchall()
            session['user_id'] = new_user[0][0]
            return redirect('/home')

#update user password
#checks user email and password exists, then replaces old password with new
@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        email = request.form.get('uemail')
        password = request.form.get('upassword')
        new_password = request.form.get('new_password')
        db.cursor.execute(f'''SELECT * FROM `users` WHERE `email` LIKE '{email}' AND `password` LIKE '{password}';''')
        check_credentials = db.cursor.fetchall()
        if len(check_credentials) == 0:
            flash("User not found. Please try again", category='error')
            return render_template('profile.html', flash=flash)
        elif len(new_password) < 5:
            flash("Password must be at least 5 characters long", category='error')
            return render_template('profile.html', flash=flash)
        else:
            db.cursor.execute(f'''UPDATE `users` SET `password` = '{new_password}' WHERE `email` = '{email}' AND `password` = '{password}';''')
            db.connection.commit()
            flash("Password updated", category='success')
            return render_template('profile.html', flash=flash)

#delete user
#checks user email and password exists, then deletes the account
#signs the user out and displays a message that the account has been deleted
@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        email = request.form.get('demail')
        password = request.form.get('dpassword')
    db.cursor.execute(f'''SELECT * FROM `users` WHERE `email` LIKE '{email}' AND `password` LIKE '{password}';''')
    check_credentials = db.cursor.fetchall()
    if len(check_credentials) == 0:
        flash("User not found. Please try again", category='error')
        return render_template('profile.html', flash=flash)
    else:
        db.cursor.execute(f'''DELETE FROM `users` WHERE `email` = '{email}' AND `password` = '{password}';''')
        session.pop('user_id')
        flash("Account successfully deleted")
        return render_template('signin.html', flash=flash)


#page for europe covid data
@app.route('/europe')
def europe():
    if 'user_id' in session:
        data = covid_data.europe()
        iso = data[0]
        country = data[1]
        country_cases = data[2]
        return render_template("europe.html", europe=data, iso=iso, country=country, country_cases=country_cases)
    else:
        return redirect("/")

#page for ireland covid data
@app.route("/ireland")
def ireland():
    if 'user_id' in session:
        ireland_data = covid_data.ireland()
        days = ireland_data[0]
        cases = ireland_data[1]
        deaths = ireland_data[2]
        recovered = ireland_data[3]
        active = ireland_data[4]
        ireland_counties = covid_data.ireland_counties()
        county_name = ireland_counties[0]
        county_cases= ireland_counties[1]
        return render_template("ireland.html", ireland=ireland_data, days=days, cases=cases, deaths=deaths, recovered = recovered, active=active,
        ireland_counties=ireland_counties, county_name=county_name, county_cases = county_cases)                                                      
    else:
        return redirect("/")


#creates a db table for users if it doesn't already exist.
if __name__ == '__main__':
    db.createDB()
    app.run(host='0.0.0.0', port='8080',ssl_context=('../cert.pem', '../privkey.pem'))

