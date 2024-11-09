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
from auth import auth_bp
from flask_sqlalchemy import SQLAlchemy
from auth.models import db, User
import bleach

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pass@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'your_secret_key'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth_bp.login'


app.register_blueprint(auth_bp, url_prefix="/auth")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def home():
    return f'Hello, {current_user.id}! <br> <a href="/auth/logout">Logout</a>'

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
