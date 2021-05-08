from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static', static_folder='static/')


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
    return f"The email is {email} and the password is {password}"

if __name__ == '__main__':
    app.run(debug=True)
