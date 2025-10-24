from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine

DATABASE = "sqlite://database.db"

login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return ""


engine = create_engine(DATABASE)

class Base(DeclarativeBase):
    pass