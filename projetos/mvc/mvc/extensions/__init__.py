from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

DATABASE = "sqlite:///database.db"

engine = create_engine(DATABASE)
Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

def init_db():
    import mvc.models
    Base.metadata.create_all(engine)


login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    from mvc.models import User
    with Session() as session:
        user = session.get(User, int(user_id))

    return user
