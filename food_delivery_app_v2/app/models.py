# app/models.py
from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))

class Customer(UserMixin, db.Model):
    CustomerID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    PhoneNumber = db.Column(db.String(15))
    Address = db.Column(db.String(255))
    Password = db.Column(db.String(255), nullable=False)
    orders = db.relationship('Order', backref='customer', lazy=True)

    def set_password(self, password):
        self.Password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.Password, password)
    
    def get_id(self):
        """Override Flask-Login's get_id method to return CustomerID."""
        return self.CustomerID
    
    @staticmethod
    def get_by_id(customer_id):
        return Customer.query.get(customer_id)
    
    @staticmethod
    def get_by_email(email):
        return Customer.query.filter_by(Email=email).first()

class Restaurant(db.Model):
    RestaurantID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Location = db.Column(db.String(255))
    ContactNumber = db.Column(db.String(15))
    CuisineType = db.Column(db.String(100))
    Rating = db.Column(db.Float, default=0.0)
    menu_items = db.relationship('MenuItem', backref='restaurant', lazy=True)
    
    def get_id(self):
        return self.RestaurantID

class MenuItem(db.Model):
    MenuItemID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Description = db.Column(db.Text)
    Category = db.Column(db.String(100))
    Rating = db.Column(db.Float, default=0.0)
    RestaurantID = db.Column(db.Integer, db.ForeignKey('restaurant.RestaurantID'), nullable=False)
    order_items = db.relationship('OrderItem', backref='menu_item', lazy=True)

class Order(db.Model):
    OrderID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    OrderDate = db.Column(db.DateTime, default=datetime.utcnow)
    TotalAmount = db.Column(db.Float)
    Status = db.Column(db.String(50))
    TimeToReach = db.Column(db.Time)
    Rating = db.Column(db.Float, default=0.0)
    CustomerID = db.Column(db.Integer, db.ForeignKey('customer.CustomerID'), nullable=False)
    RestaurantID = db.Column(db.Integer, db.ForeignKey('restaurant.RestaurantID'), nullable=False)
    order_items = db.relationship('OrderItem', backref='order', lazy=True)
    payment = db.relationship('Payment', backref='order', uselist=False)

class OrderItem(db.Model):
    OrderItemID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Quantity = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Float, nullable=False)
    MenuItemID = db.Column(db.Integer, db.ForeignKey('menu_item.MenuItemID'), nullable=False)
    OrderID = db.Column(db.Integer, db.ForeignKey('order.OrderID'), nullable=False)

class DeliveryPerson(db.Model):
    DeliveryPersonID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    PhoneNumber = db.Column(db.String(15))
    VehicleDetails = db.Column(db.String(100))
    Rating = db.Column(db.Float, default=0.0)

class Payment(db.Model):
    PaymentID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PaymentDate = db.Column(db.DateTime, default=datetime.utcnow)
    PaymentMethod = db.Column(db.String(50))
    PaymentStatus = db.Column(db.String(50))
    Amount = db.Column(db.Float)
    OrderID = db.Column(db.Integer, db.ForeignKey('order.OrderID'), nullable=False)