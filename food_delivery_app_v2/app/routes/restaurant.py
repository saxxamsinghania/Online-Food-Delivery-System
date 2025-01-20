# app/routes/restaurant.py
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from app.models import Restaurant, MenuItem
from app import db
from sqlalchemy import asc

bp = Blueprint('restaurant', __name__, url_prefix='/restaurant')

@bp.route('/<int:restaurant_id>/menu')
@login_required
def menu(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    
    menu_items = (MenuItem.query
                 .join(Restaurant)
                 .filter(MenuItem.RestaurantID == restaurant_id)
                 .order_by(MenuItem.Category, MenuItem.Name)
                 .add_columns(
                     MenuItem.MenuItemID,
                     MenuItem.Name.label('MenuItemName'),
                     MenuItem.Price,
                     MenuItem.Description,
                     MenuItem.Category,
                     MenuItem.Rating,
                     MenuItem.RestaurantID,
                     Restaurant.Name.label('RestaurantName')
                 ).all())
    
    # Group items by category
    categories = {}
    for item in menu_items:
        if item.Category not in categories:
            categories[item.Category] = []
        categories[item.Category].append(item)
    
    return render_template('restaurant/menu.html',
                         restaurant=restaurant,
                         categories=categories)
