from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static/')


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")




if __name__ == '__main__':
    app.run(debug=True)
