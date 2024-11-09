from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from src.encoder import *

auth_bp = Blueprint('auth_bp', __name__)

users = {
    'user1': {'password': 'password1'},
    'user2': {'password': 'password2'}
}


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        # Check if the user exists and password is correct
        if user and verify_password_bcrypt(user.password, password):  # Check if password matches
            login_user(user)  # Log the user in
            flash('Login successful!', 'success')
            return redirect(url_for('home'))  # Redirect to the home page
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out successfully', 'info')
    return redirect(url_for('auth.login'))
