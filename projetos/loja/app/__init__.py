from flask import (
    Flask,
    render_template
)
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()

def create_app(drop_tables:bool = False):
    app = Flask(__name__)
    app.secret_key = 'depois mudar isso, preguiça'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    # app.secret_key = os.getenv('SECRET_KEY')
    
    db.init_app(app)
    
    from .models import User

    with app.app_context():
        if drop_tables:
            db.drop_all()
            db.create_all()

            from werkzeug.security import generate_password_hash
            db.session.add(User(name='ZagZ', email='zezi@example.com', password_hash=generate_password_hash('123')))
            db.session.commit()

            user:User = User.query.get(1) # trocar por db.session.get()???
            print(f'\n{user.id} {user.name} {user.email}\n')        
        else:
            db.create_all()

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        return render_template('auth/login.html')
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        return render_template('auth/register.html')
    

    return app