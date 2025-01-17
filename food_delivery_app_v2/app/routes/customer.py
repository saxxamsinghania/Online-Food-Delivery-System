# app/routes/customer.py
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from app.models import *
from app import mysql

bp = Blueprint('customer', __name__, url_prefix='/customer')

@bp.route('/dashboard')
@login_required
def dashboard():
    # Get restaurants
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Restaurant ORDER BY Rating DESC')
    restaurants = cur.fetchall()
    
    # Get user's orders
    cur.execute('''
        SELECT o.*, r.Name as restaurant_name 
        FROM `Order` o 
        JOIN Restaurant r ON o.RestaurantID = r.RestaurantID 
        WHERE o.CustomerID = %s 
        ORDER BY o.OrderDate DESC
    ''', (current_user.get_id,))
    orders = cur.fetchall()
    cur.close()
    
    return render_template('customer/dashboard.html', 
                         restaurants=restaurants, 
                         orders=orders)

@bp.route('/place-order', methods=['POST'])
@login_required
def place_order():
    data = request.get_json()
    
    # Extract restaurant_id from the first item in the items list
    restaurant_id = data['items'][0]['RestaurantID']
    items = data['items']
    
    # Ensure that the restaurant_id is consistent across all items
    for item in items:
        if item['RestaurantID'] != restaurant_id:
            return {'success': False, 'error': 'Items belong to different restaurants.'}, 400
    
    # Calculate total amount
    total_amount = sum(float(item['Price']) * item['Quantity'] for item in items)
    print(total_amount)
    cur = mysql.connection.cursor()
    try:
        # Create order
        cur.execute('''
            INSERT INTO `Order` (CustomerID, RestaurantID, TotalAmount, Status, OrderDate)
            VALUES (%s, %s, %s, 'Pending', NOW())
        ''', (current_user.get_id(), restaurant_id, total_amount))
        
        order_id = cur.lastrowid
        
        # Create order items
        for item in items:
            cur.execute('''
                INSERT INTO order_item (OrderID, MenuItemID, Quantity, Price)
                VALUES (%s, %s, %s, %s)
            ''', (order_id, item['MenuItemID'], item['Quantity'], item['Price']))
        
        mysql.connection.commit()
        return {'success': True, 'order_id': order_id}
    except Exception as e:
        mysql.connection.rollback()
        return {'success': False, 'error': str(e)}, 500
    finally:
        cur.close()

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
    print("Here ji")
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
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    return jsonify({
        'cart': [item.to_dict() for item in cart_items]
    })
