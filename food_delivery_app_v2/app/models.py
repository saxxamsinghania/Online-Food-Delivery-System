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

class Payment(db.Model):
    PaymentID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PaymentDate = db.Column(db.DateTime, default=datetime.utcnow)
    PaymentMethod = db.Column(db.String(50))
    PaymentStatus = db.Column(db.String(50))
    Amount = db.Column(db.Float)
    OrderID = db.Column(db.Integer, db.ForeignKey('order.OrderID'), nullable=False)
class CartItem(db.Model):
    CartItemID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('customer.CustomerID'), nullable=False)
    MenuItemID = db.Column(db.Integer, db.ForeignKey('menu_item.MenuItemID'), nullable=False)
    # Name = db.Column(db.String(100), db.ForeignKey('menu_item.Name'), nullable=False)
    # Price = db.Column(db.Float, db.ForeignKey('menu_item.Price'), nullable=False)
    RestaurantID = db.Column(db.Integer, db.ForeignKey('restaurant.RestaurantID'), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False, default=1)
    
    # Relationships
    customer = db.relationship('Customer', backref=db.backref('cart_items', lazy=True))
    menu_item = db.relationship('MenuItem', backref=db.backref('cart_items', lazy=True))
    Restaurant = db.relationship('Restaurant', backref=db.backref('cart_items',lazy=True))

    @classmethod
    def get_cart_items(cls, customer_id):
        """
        Retrieve all cart items for a specific customer
        """
        return cls.query.filter_by(CustomerID=customer_id).all()

    @classmethod
    def add_to_cart(cls, customer_id, menu_item_id, restaurant_id, quantity=1):
        """
        Add an item to the cart or update its quantity
        """
        existing_item = cls.query.filter_by(
            CustomerID=customer_id, 
            MenuItemID=menu_item_id
        ).first()

        if existing_item:
            existing_item.Quantity += quantity
        else:
            new_cart_item = cls(
                CustomerID=customer_id, 
                MenuItemID=menu_item_id, 
                Quantity=quantity,
                RestaurantID = restaurant_id
            )
            db.session.add(new_cart_item)
        
        db.session.commit()
        return existing_item or new_cart_item

    @classmethod
    def remove_from_cart(cls, customer_id, menu_item_id, quantity=1):
        """
        Remove an item from the cart or reduce its quantity
        """
        cart_item = cls.query.filter_by(
            CustomerID=customer_id, 
            MenuItemID=menu_item_id
        ).first()

        if cart_item:
            cart_item.Quantity -= quantity
            if cart_item.Quantity <= 0:
                db.session.delete(cart_item)
            db.session.commit()
        
        return cart_item

    @classmethod
    def clear_cart(cls, customer_id):
        """
        Remove all items from a customer's cart
        """
        cls.query.filter_by(CustomerID=customer_id).delete()
        db.session.commit()

    # def to_dict(self):
    #     """
    #     Convert cart item to dictionary for easy serialization
    #     """
    #     return {
    #         'id': self.MenuItemID,
    #         'name': self.menu_item.Name,
    #         'price': self.menu_item.Price,
    #         'restaurant': self.menu_item.restaurant.Name,
    #         'RestaurantID': self.menu_item.RestaurantID,
    #         'quantity': self.Quantity
        # }
    def to_dict(self):
        """
        Convert the CartItem object to a dictionary
        """
        return {
            "id": self.CartItemID,
            "CustomerID": self.CustomerID,
            "MenuItemID": self.MenuItemID,
            "Name": self.menu_item.Name,
            "Price": self.menu_item.Price,
            "Quantity": self.Quantity,
            "RestaurantID": self.Restaurant.RestaurantID,
            'restaurant': self.Restaurant.Name
            # "MenuItem": {
            #     "Name": self.menu_item.Name,
            #     "Price": self.menu_item.Price
            # }
        }
