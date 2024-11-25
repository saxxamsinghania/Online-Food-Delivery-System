# app/routes/customer.py
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models import Restaurant, Order
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
    total_amount = sum(float(item['price']) * item['quantity'] for item in items)
    
    cur = mysql.connection.cursor()
    try:
        # Create order
        cur.execute('''
            INSERT INTO `Order` (CustomerID, RestaurantID, TotalAmount, Status)
            VALUES (%s, %s, %s, 'Pending')
        ''', (current_user.get_id(), restaurant_id, total_amount))
        
        order_id = cur.lastrowid
        
        # Create order items
        for item in items:
            cur.execute('''
                INSERT INTO OrderItem (OrderID, MenuItemID, Quantity, Price)
                VALUES (%s, %s, %s, %s)
            ''', (order_id, item['id'], item['quantity'], item['price']))
        
        mysql.connection.commit()
        return {'success': True, 'order_id': order_id}
    except Exception as e:
        mysql.connection.rollback()
        return {'success': False, 'error': str(e)}, 500
    finally:
        cur.close()
