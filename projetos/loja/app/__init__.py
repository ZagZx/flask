from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    get_flashed_messages
)
from flask_login import (
    LoginManager, 
    login_user, 
    logout_user,
    login_required, 
    current_user
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import pymysql


login_manager = LoginManager()
db = SQLAlchemy()

DB_NAME = "miniprojeto_sqlalchemy"
DB_URL = f"mysql+pymysql://root:@127.0.0.1/{DB_NAME}"

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password=''
)

with conn.cursor() as cursor:
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

conn.close()


def create_app(drop_tables:bool = False):
    app = Flask(__name__)
    app.secret_key = 'depois mudar isso, preguiça'
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
    # app.secret_key = os.getenv('SECRET_KEY')
    
    db.init_app(app)
    
    from .models import User, Product

    with app.app_context():
        if drop_tables:
            db.drop_all()
            db.create_all()     
        else:
            db.create_all()
        
        if not User.query.all():
            db.session.add(User(name='ZagZ', email='zezi@example.com', password_hash=generate_password_hash('123')))
            db.session.commit()
            user:User = User.query.get(1) # trocar por db.session.get()???
            print(f'\n{user.id} {user.name} {user.email}\n')

    login_manager.init_app(app)
    login_manager.login_view = 'login'
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    @app.route('/')
    def index():
        # users:list[User] = User.query.all()
        # for user in users:
        #     print(user.name, user.email)

        products:list[Product] = Product.query.all()
        for product in products:
            print(product.name, product.price, product.description)
        
        return render_template('index.html')
    
    @app.route('/products/add', methods=['GET', 'POST'])
    @login_required
    def add_product():
        if request.method == 'POST':
            name = request.form.get('name')
            description = request.form.get('description')
            price = request.form.get('price')
            price = price.replace(',', '.')

            # print(name, float(price), description)

            product = Product(name=name, price=price, description=description)
            db.session.add(product)
            db.session.commit()
        return render_template('products/add.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')

            user:User = User.query.filter_by(email=email).first()
            
            if user:            
                if check_password_hash(user.password_hash, password):
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    flash('Senha incorreta', 'error')
            else:
                flash('O usuário não está cadastrado', 'error')
        return render_template('auth/login.html')
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')


            print(name, email, password)
            if User.query.filter_by(email=email).first():
                flash('Já existe um usuário cadastrado com esse email', 'error')
            if User.query.filter_by(name=name).first():
                flash('Já existe um usuário com esse nome', 'error')

            if name and email and password:
                if not get_flashed_messages(category_filter='error'):
                    password_hash = generate_password_hash(password)

                    user:User = User(name=name, email=email, password_hash=password_hash)
                    db.session.add(user)
                    db.session.flush()
                    db.session.commit()

                    return redirect(url_for('login'))
                return render_template('auth/register.html')
        return render_template('auth/register.html')
    
    @app.route('/logout', methods=['GET', 'POST'])
    def logout():
        logout_user()
        return redirect(url_for('index'))
    

    return app