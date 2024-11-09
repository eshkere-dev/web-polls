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
import bleach

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

users = {
    'user1': {'password': 'password1'},
    'user2': {'password': 'password2'}
}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id in users else None

def is_logged():
    return True


@app.route('/createsurvey', methods=['POST'])
def create_survey():
    data = request.get_json()
    action = data.get('action')
    if action == "create_survey":
        if is_logged():
            return redirect('/create_survey')
        else:
            return redirect('/login')


@app.route('/')
def start():  # put application's code here
    return render_template("index.html")


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
