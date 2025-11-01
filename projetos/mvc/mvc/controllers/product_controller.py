from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from mvc.extensions import db
from mvc.models import Product, User

current_user: User

product_bp = Blueprint('product', __name__)

@product_bp.route('/vender', methods=['GET', 'POST'])
@login_required
def sell():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')

        if name and description and price:
            product = Product(name=name, description=description, price=price, seller = current_user)
            db.session.add(product)
            db.session.commit()
            return redirect(url_for('product.my_sales'))
        else:
            flash('Preencha todos os campos do formulário', 'error')

    return render_template('products/sell.html')

@product_bp.route('/comprar/<int:id>', methods=['POST'])
@login_required
def buy(id):
    product: Product = Product.query.get(id)
    product.purchaser = current_user
    product.avaliable = False
    
    db.session.commit()

    return redirect(url_for('index'))

@product_bp.route('/meus-pedidos')
@login_required
def my_orders():
    products: list[Product] = Product.query.where(Product.purchaser == current_user).all()

    return render_template('products/my_orders.html', products=products)

@product_bp.route('/minhas-vendas')
@login_required
def my_sales():
    products: list[Product] = current_user.sold_products

    return render_template('products/my_sales.html', products=products)