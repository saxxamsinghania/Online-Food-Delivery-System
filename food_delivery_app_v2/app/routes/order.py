# app/routes/order.py
import qrcode
from flask import Blueprint, render_template, request, jsonify, send_file
from flask_login import login_required, current_user
from app import mysql
from app.models import *
from datetime import datetime
from decimal import Decimal

bp = Blueprint('order', __name__, url_prefix='/order')

@bp.route('/<int:order_id>')
@login_required
def order_details(order_id):
    cur = mysql.connection.cursor()
    
    customer = Customer.get_by_id(current_user.get_id())
    if not customer:
        return 'Customer not found', 404
    
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
        FROM order_item oi 
        JOIN menu_item mi ON oi.MenuItemID = mi.MenuItemID 
        WHERE oi.OrderID = %s
    ''', (order_id,))
    items = cur.fetchall()
    
    total_amount = Decimal(str(order['TotalAmount']))
    gst = total_amount * Decimal('0.05')
    delivery_fee = Decimal('60.00')
    rest_packaging_charges = Decimal('50.00')
    platform_fee = Decimal('10.00')
    
    grand_total= total_amount+gst+rest_packaging_charges+platform_fee+delivery_fee
    cur.close()
    
    return render_template('customer/order.html', order=order, items=items, gst=gst, grand_total=grand_total, orderId = order_id, customer_address=customer.Address)


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
        ''', (rating, order_id, current_user.CustomerID))
        mysql.connection.commit()
        return jsonify({'success': True})
    except Exception as e:
        mysql.connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cur.close()


@bp.route('/generate-qr', methods=['POST'])
def generate_qr():
    try:
        upi_id = 'saksham1225@oksbi'
        payee_name = 'Saksham Singhania' 
        amount = request.get_json()['total_amount']  
        
        transaction_note = "Online Food Delivery"
        
        upi_uri = f"upi://pay?pa={upi_id}&pn={payee_name}&am={amount}&cu=INR&tn={transaction_note}"
        qr = qrcode.make(upi_uri)
        qr.save("app/static/img/qr-code.png")  

        return {'success': True}, 200
    except Exception as e:
        return {'success': False, 'error': str(e)}, 500



@bp.route('/process-payment/<int:order_id>')
@login_required
def process_payment(order_id):
    
    cur = mysql.connection.cursor()

    cur.execute(''' SELECT o.* 
                FROM `Order` o 
                WHERE o.OrderID = %s AND o.CustomerID = %s
    ''', (order_id, current_user.get_id()))
    order = cur.fetchone()
    
    if not order:
        return 'Order not found', 404
    
    return render_template('customer/payment.html', order=order)
    
@bp.route('/complete-order/<int:order_id>', methods=['POST'])
@login_required
def complete_order(order_id):
    data = request.get_json()
    amount = data['amount']
    paymentMethod = data['paymentMethod']
    print("Hereeeeee")
    cur = mysql.connection.cursor()
    
    try:
        cur.execute('''
                INSERT INTO Payment (PaymentDate, PaymentMethod, PaymentStatus, Amount, OrderID)
                VALUES (NOW(), %s, 'Completed', %s, %s)
            ''', (paymentMethod, amount, order_id))
        mysql.connection.commit()
        return {'success': True, 'order_id': order_id}
    except Exception as e:
        mysql.connection.rollback()
        return {'success': False, 'error': str(e)}, 500
    finally:
        cur.close()
        
@bp.route('order-confirmed/<int:order_id>', methods=['GET'])
@login_required
def order_confirmation(order_id):
    
    try:
        customer = Customer.get_by_id(current_user.get_id())
        print(customer.Address)
        if not customer:
            return 'Customer not found', 404
        # Fetch the order details
        order = Order.query.get_or_404(order_id)
        cur = mysql.connection.cursor()

        # Fetch the corresponding payment
        payment = Payment.query.filter_by(OrderID=order_id).first()

        if not payment:
            return render_template('customer/payment.html', order=order), 404
        
        # Get order items
        cur.execute('''
            SELECT oi.*, mi.Name, mi.Description 
            FROM order_item oi 
            JOIN menu_item mi ON oi.MenuItemID = mi.MenuItemID 
            WHERE oi.OrderID = %s
        ''', (order_id,))
        items = cur.fetchall()
       
        for item in items:
            print(item)

        return render_template(
            'customer/order_confirmation.html', 
            order=order, 
            payment=payment, 
            items=items,
            customer_address = customer.Address
        )
    
    except Exception as e:
        # Log the error
        print(f"Error in order confirmation: {e}")
        return render_template('customer/order.html', order=order), 404
