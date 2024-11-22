# app/routes/order.py
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app import mysql
from datetime import datetime

bp = Blueprint('order', __name__, url_prefix='/order')

@bp.route('/<int:order_id>')
@login_required
def order_details(order_id):
    cur = mysql.connection.cursor()
    
    # Get order details
    cur.execute('''
        SELECT o.*, r.Name as restaurant_name 
        FROM `Order` o 
        JOIN Restaurant r ON o.RestaurantID = r.RestaurantID 
        WHERE o.OrderID = %s AND o.CustomerID = %s
    ''', (order_id, current_user.get_id()))
    order = cur.fetchone()
    
    if not order:
        return 'Order not found', 404
    
    # Get order items
    cur.execute('''
        SELECT oi.*, mi.Name, mi.Description 
        FROM OrderItem oi 
        JOIN MenuItem mi ON oi.MenuItemID = mi.MenuItemID 
        WHERE oi.OrderID = %s
    ''', (order_id,))
    items = cur.fetchall()
    cur.close()
    
    # return render_template('order/details.html', order=order, items=items)
    return render_template('customer/order.html', order=order, items=items)

@bp.route('/<int:order_id>/rate', methods=['POST'])
@login_required
def rate_order(order_id):
    rating = request.json.get('rating')
    if not 1 <= rating <= 5:
        return jsonify({'error': 'Invalid rating'}), 400
    
    cur = mysql.connection.cursor()
    try:
        cur.execute('''
            UPDATE `Order` 
            SET Rating = %s 
            WHERE OrderID = %s AND CustomerID = %s
        ''', (rating, order_id, current_user.id))
        mysql.connection.commit()
        return jsonify({'success': True})
    except Exception as e:
        mysql.connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cur.close()


@bp.route('/process-payment', methods=['POST'])
@login_required
def process_payment():
    data = request.json
    order_id = data['order_id']
    payment_method = data['payment_method']
    
    if order_id in orders:
        # Simulate payment processing
        orders[order_id]['status'] = 'paid'
        orders[order_id]['payment_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return jsonify({
            'success': True,
            'order_id': order_id,
            'message': 'Payment successful'
        })
    
    return jsonify({
        'success': False,
        'message': 'Order not found'
    })
        