from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from mvc.extensions import db
from mvc.models import Product

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

@product_bp.route('/meus_pedidos')
@login_required
def my_orders():
    return render_template('products/my_orders.html')

@product_bp.route('/minhas_vendas')
@login_required
def my_sales():
    return render_template('products/my_sales.html')