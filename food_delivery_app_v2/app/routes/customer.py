# app/routes/customer.py
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from app.models import *
from app import db

bp = Blueprint('customer', __name__, url_prefix='/customer')

@bp.route('/dashboard')
@login_required
def dashboard():
    # Get restaurants ordered by rating
    restaurants = Restaurant.query.order_by(Restaurant.Rating.desc()).all()
    
    # Get user's orders with restaurant information
    orders = (Order.query
             .join(Restaurant)
             .filter(Order.CustomerID == current_user.CustomerID)
             .order_by(Order.OrderDate.desc())
             .add_columns(Restaurant.Name.label('restaurant_name'))
             .all())
    
    return render_template('customer/dashboard.html', 
                         restaurants=restaurants, 
                         orders=orders)

@bp.route('/place-order', methods=['POST'])
@login_required
def place_order():
    data = request.get_json()
    restaurant_id = data['items'][0]['RestaurantID']
    items = data['items']
    
    # Ensure that the restaurant_id is consistent across all items
    for item in items:
        if item['RestaurantID'] != restaurant_id:
            return {'success': False, 'error': 'Items belong to different restaurants.'}, 400
    
    # Calculate total amount
    total_amount = sum(float(item['Price']) * item['Quantity'] for item in items)
    
    try:
        # Create new order
        new_order = Order(
            CustomerID=current_user.CustomerID,
            RestaurantID=restaurant_id,
            TotalAmount=total_amount,
            Status='Pending'
        )
        db.session.add(new_order)
        db.session.flush()  # This gets us the new order ID
        
        # Create order items
        for item in items:
            order_item = OrderItem(
                OrderID=new_order.OrderID,
                MenuItemID=item['MenuItemID'],
                Quantity=item['Quantity'],
                Price=item['Price']
            )
            db.session.add(order_item)
        
        db.session.commit()
        return {'success': True, 'order_id': new_order.OrderID}
    
    except Exception as e:
        db.session.rollback()
        return {'success': False, 'error': str(e)}, 500

@bp.route('/restaurant/<int:id>')
def restaurant_detail(id):
    restaurant = Restaurant.query.get_or_404(id)
    return render_template('restaurant_detail.html', restaurant=restaurant)

@bp.route('/orders')
@login_required
def orders():
    orders = Order.query.filter_by(CustomerID=current_user.CustomerID).all()
    return render_template('orders.html', orders=orders)

@bp.route('/add_to_cart/<int:menu_item_id>', methods=['POST'])
@login_required
def add_to_cart(menu_item_id):
    data = request.get_json()
    restaurant_id = data['RestaurantID']
    menu_item = MenuItem.query.get_or_404(menu_item_id)
    CartItem.add_to_cart(current_user.CustomerID, menu_item_id, restaurant_id)
    return jsonify({'success': True})

@bp.route('/cart')
@login_required
def cart():
    cart_items = CartItem.get_cart_items(current_user.CustomerID)
    cart_items_dict = [item.to_dict() for item in cart_items]
    return jsonify(cart_items_dict)

@bp.route('/remove_from_cart/<int:menu_item_id>', methods=['POST'])
@login_required
def remove_from_cart(menu_item_id):
    CartItem.remove_from_cart(current_user.CustomerID, menu_item_id)
    return jsonify({'success': True})

@bp.route('/clear_cart', methods=['POST'])
@login_required
def clear_cart():
    CartItem.clear_cart(current_user.CustomerID)
    return jsonify({'success': True})

@bp.route('/customer/get-cart')
@login_required
def get_cart():
    cart_items = CartItem.query.filter_by(CustomerID=current_user.CustomerID).all()
    return jsonify({
        'cart': [item.to_dict() for item in cart_items]
    })
