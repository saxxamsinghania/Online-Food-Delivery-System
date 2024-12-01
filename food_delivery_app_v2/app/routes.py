# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models import *
from app.forms import LoginForm, RegistrationForm
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    restaurants = Restaurant.query.all()
    return render_template('home.html', restaurants=restaurants)

# @main.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = Customer(
#             Name=form.name.data,
#             Email=form.email.data,
#             PhoneNumber=form.phone.data,
#             Address=form.address.data
#         )
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Registration successful!')
#         return redirect(url_for('main.login'))
#     return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Customer.query.filter_by(Email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        flash('Invalid email or password')
    return render_template('login.html', form=form)

@main.route('/restaurant/<int:id>')
def restaurant_detail(id):
    restaurant = Restaurant.query.get_or_404(id)
    return render_template('restaurant_detail.html', restaurant=restaurant)


@main.route('/place_order', methods=['POST'])
@login_required
def place_order():
    # Implementation for placing order
    pass

@main.route('/orders')
@login_required
def orders():
    orders = Order.query.filter_by(CustomerID=current_user.CustomerID).all()
    return render_template('orders.html', orders=orders)

@main.route('/add_to_cart/<int:menu_item_id>', methods=['POST'])
@login_required
def add_to_cart(menu_item_id):
    menu_item = MenuItem.query.get_or_404(menu_item_id)
    print("Here ji")
    CartItem.add_to_cart(current_user.CustomerID, menu_item_id)
    return jsonify({'success': True})

@main.route('/cart')
@login_required
def cart():
    cart_items = CartItem.get_cart_items(current_user.CustomerID)
    return render_template('cart.html', cart_items=cart_items)

@main.route('/remove_from_cart/<int:menu_item_id>', methods=['POST'])
@login_required
def remove_from_cart(menu_item_id):
    CartItem.remove_from_cart(current_user.CustomerID, menu_item_id)
    return jsonify({'success': True})

@main.route('/clear_cart', methods=['POST'])
@login_required
def clear_cart():
    CartItem.clear_cart(current_user.CustomerID)
    return jsonify({'success': True})