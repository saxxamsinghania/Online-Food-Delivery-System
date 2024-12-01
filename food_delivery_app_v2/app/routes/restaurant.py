# app/routes/restaurant.py
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from app.models import Restaurant, MenuItem
from app import mysql

bp = Blueprint('restaurant', __name__, url_prefix='/restaurant')

@bp.route('/<int:restaurant_id>/menu')
@login_required
def menu(restaurant_id):
    cur = mysql.connection.cursor()
    
    cur.execute('SELECT * FROM Restaurant WHERE RestaurantID = %s', (restaurant_id,))
    restaurant = cur.fetchone()
    
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    cur.execute('''
        SELECT mi.MenuItemID, mi.Name AS MenuItemName, mi.Price, mi.Description, mi.Category, 
               mi.Rating, mi.RestaurantID, r.Name AS RestaurantName
        FROM menu_item mi
        JOIN Restaurant r ON mi.RestaurantID = r.RestaurantID
        WHERE mi.RestaurantID = %s
        ORDER BY mi.Category, mi.Name
    ''', (restaurant_id,))
    menu_items = cur.fetchall()
    cur.close()
    
    # Group items by category
    categories = {}
    for item in menu_items:
        if item['Category'] not in categories:
            categories[item['Category']] = []
        categories[item['Category']].append(item)
    
    return render_template('restaurant/menu.html',
                         restaurant=restaurant,
                         categories=categories)