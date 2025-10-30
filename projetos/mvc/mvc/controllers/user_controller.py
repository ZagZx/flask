from flask import Blueprint, redirect, url_for, render_template, request, flash
from flask_login import login_required, logout_user, login_user
from werkzeug.security import generate_password_hash

from mvc.models import User
from mvc.extensions import Session


user_bp = Blueprint('user', __name__, url_prefix='/usuario')

@user_bp.route('/sair')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        with Session() as session:
            user:User = session.query(User).filter_by(email=email).first()
        
        if user:
            if user.check_password(password):
                login_user(user)
                return redirect(url_for('index'))
        flash('Email ou senha incorreta','error')
    return render_template('auth/login.html')

@user_bp.route('/cadastro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        with Session() as session:
            user:User = session.query(User).filter_by(email=email).first()
        
            if user:
                flash(f'O email {email} já está cadastrado','error')
                return redirect(url_for('user.register'))
            
            if username and email and password:
                user = User(username=username, email=email, password_hash=generate_password_hash(password))
                session.add(user)
                session.commit()
            else:
                flash('Preencha todos os dados do formulário', 'error')
        
    return render_template('auth/register.html')
