from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required, logout_user, login_user

user_bp = Blueprint('user', __name__, url_prefix='/usuario')

@user_bp.route('/sair')
@login_required
def logout():
    return redirect(url_for('index'))

@user_bp.route('/login')
def login():
    return render_template('auth/login.html')

@user_bp.route('/cadastro')
def register():
    return render_template('auth/register.html')
