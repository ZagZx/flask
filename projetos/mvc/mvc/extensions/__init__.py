from flask_login import LoginManager
from flask import Flask
# from sqlalchemy.orm import DeclarativeBase, sessionmaker
# from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
# from mvc.config import DATABASE

db = SQLAlchemy()

def init_db(app: Flask):
    import mvc.models
    with app.app_context():
        db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message = 'Faça login para realizar essa ação'
login_manager.login_message_category = 'warning'
@login_manager.user_loader
def load_user(user_id):
    from mvc.models import User
    user = User.query.get(int(user_id))

    return user
