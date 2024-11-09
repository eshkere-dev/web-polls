from flask import Flask, render_template, redirect, url_for, flash, request
import bleach

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

def clear_input(input):
    return bleach.clean(input)

@app.route('/login')
def register():
    return render_template("login.html")

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        password = request.form['password']
        confirm_password = request.form['confirm_password']


        if password != confirm_password:
            flash("Passwords do not match!")
            return redirect



if __name__ == '__main__':
    app.run(debug=True)