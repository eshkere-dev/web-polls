import os

from flask import (Flask,
                   render_template,
                   redirect,
                   url_for,
                   flash,
                   request)
from flask_login import (LoginManager,
                         UserMixin,
                         login_user,
                         login_required,
                         logout_user,
                         current_user)
import src.databaseManager as db
import src.encoder as enc

import bleach

app = Flask(__name__)

app.secret_key = "Hello World!"


@app.route('/')
def home():
    return render_template(url_for('index'))


@app.route('/createsurvey/', methods=['POST'])
def create_survey():
    data = request.get_json()
    action = data.get('action')
    if action == "create_survey":
        return redirect('/create_survey')


@app.route('/')
def start():
    return render_template("index.html")


@app.route('/login/', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            username = request.form["username"]
            email = request.form['email']
            password = request.form['password']
            password_confirm = request.form['password_repeat']

            if password != password_confirm:
                return render_template('login.html', error="Passwords do not match. Please try again")

            if db.add_user(email,
                           username,
                           enc.hash_password_bcrypt(password)):
                flash("Registration successful!")
                return redirect(url_for('index'))
        except:
            pass

    return render_template("login.html")


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash("Passwords do not match!")
            return redirect


if __name__ == '__main__':
    app.run(debug=True)
