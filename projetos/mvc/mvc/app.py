from flask import Flask, render_template
from mvc.extensions import login_manager, db, init_db
from mvc.config import SECRET_KEY, DATABASE
from mvc.models import Product

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE

login_manager.init_app(app)
db.init_app(app)
init_db(app)


@app.route('/')
def index():
    products: list[Product] = Product.query.where(Product.avaliable == True).all()

    return render_template('index.html', products=products)

from mvc.controllers import user_bp, product_bp

app.register_blueprint(user_bp)
app.register_blueprint(product_bp)