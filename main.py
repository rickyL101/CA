from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static/')



@app.route('/')
def signin():
    return render_template("signin.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/home')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
