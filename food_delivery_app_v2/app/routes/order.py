# app/routes/order.py
from flask import Blueprint, render_template, request, jsonify, send_file
from flask_login import login_required, current_user
from app.models import *
from app import db
import qrcode
from datetime import datetime
from decimal import Decimal

bp = Blueprint('order', __name__, url_prefix='/order')
@bp.route('/<int:order_id>')
@login_required
def order_details(order_id):
    customer = Customer.query.get(current_user.CustomerID)
    if not customer:
        return 'Customer not found', 404
    
    # Get order details with restaurant
    result = (Order.query
            .join(Restaurant)
            .add_columns(
                Order.OrderID,
                Order.TotalAmount,
                Order.Status,
                Order.OrderDate,
                Restaurant.Name.label('restaurant_name')
            )
            .filter(Order.OrderID == order_id, 
                   Order.CustomerID == current_user.CustomerID)
            .first())
    
    if not result:
        return 'Order not found', 404
    
    # Create a dict with order details for easy template access
    order_dict = {
        'OrderID': result.OrderID,
        'TotalAmount': result.TotalAmount,
        'Status': result.Status,
        'OrderDate': result.OrderDate,
        'restaurant_name': result.restaurant_name
    }
    
    # Get order items with menu item details
    items_result = (db.session.query(
            OrderItem.Quantity,
            OrderItem.Price,
            MenuItem.Name,
            MenuItem.Description
        )
        .join(MenuItem)
        .filter(OrderItem.OrderID == order_id)
        .all())
    
    # Convert items to list of dicts for easy template access
    items = []
    for item in items_result:
        items.append({
            'Name': item.Name,
            'Description': item.Description,
            'Price': item.Price,
            'Quantity': item.Quantity
        })
    
    total_amount = Decimal(str(order_dict['TotalAmount']))
    gst = total_amount * Decimal('0.05')
    delivery_fee = Decimal('60.00')
    rest_packaging_charges = Decimal('50.00')
    platform_fee = Decimal('10.00')
    
    grand_total = total_amount + gst + rest_packaging_charges + platform_fee + delivery_fee
    
    return render_template('customer/order.html', 
                         order=order_dict,
                         items=items, 
                         gst=gst, 
                         grand_total=grand_total, 
                         orderId=order_id, 
                         customer_address=customer.Address)

@bp.route('/<int:order_id>/rate', methods=['POST'])
@login_required
def rate_order(order_id):
    rating = request.json.get('rating')
    
    if not 1 <= rating <= 5:
        return jsonify({'error': 'Invalid rating'}), 400
    
    try:
        order = Order.query.filter_by(
            OrderID=order_id, 
            CustomerID=current_user.CustomerID
        ).first()
        
        if order:
            order.Rating = rating
            db.session.commit()
            return jsonify({'success': True})
        return jsonify({'error': 'Order not found'}), 404
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

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
    grand_total = request.args.get('grand_total', type=float)
    
    order = Order.query.filter_by(
        OrderID=order_id, 
        CustomerID=current_user.CustomerID
    ).first()
    
    if not order:
        return 'Order not found', 404
    
    return render_template('customer/payment.html', order=order, grand_total=grand_total)

@bp.route('/complete-order/<int:order_id>', methods=['POST'])
@login_required
def complete_order(order_id):
    data = request.get_json()
    amount = data['amount']
    payment_method = data['paymentMethod']
    
    try:
        new_payment = Payment(
            PaymentMethod=payment_method,
            PaymentStatus='Completed',
            Amount=amount,
            OrderID=order_id
        )
        db.session.add(new_payment)
        db.session.commit()
        return {'success': True, 'order_id': order_id}
    except Exception as e:
        db.session.rollback()
        return {'success': False, 'error': str(e)}, 500

@bp.route('order-confirmed/<int:order_id>', methods=['GET'])
@login_required
def order_confirmation(order_id):
    try:
        customer = Customer.query.get(current_user.CustomerID)
        if not customer:
            return 'Customer not found', 404

        order = Order.query.get_or_404(order_id)
        payment = Payment.query.filter_by(OrderID=order_id).first()

        if not payment:
            return render_template('customer/payment.html', order=order), 404
        
        items_result = (OrderItem.query
                .join(MenuItem)
                .filter(OrderItem.OrderID == order_id)
                .add_columns(MenuItem.Name, MenuItem.Description)
                .all())
        
        '''
        items_result list:
        [(<OrderItem 5>, 'Green Tea Ice Cream', 'Refreshing green tea flavored dessert'), (<OrderItem 6>, 'Dragon Roll', 'Eel and cucumber roll topped with avocado')]
        '''
        # Convert items to list of dicts for easy template access
        items = []
        for item in items_result:
            items.append({'OrderItemID': item[0].OrderItemID,
                'Quantity': item[0].Quantity,
                'Price': item[0].Price,
                'OrderID': item[0].OrderID,
                'Name': item[1],
                'Description': item[2]
            })

        return render_template(
            'customer/order_confirmation.html', 
            order=order, 
            payment=payment, 
            items=items,
            customer_address=customer.Address
        )
    
    except Exception as e:
        print(f"Error in order confirmation: {e}")
        return render_template('customer/order.html', order=order), 404
