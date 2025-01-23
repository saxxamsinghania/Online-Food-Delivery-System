from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Customer

bp = Blueprint('home', __name__)

@bp.route('/')
def home():
    return render_template('homepage.html')

@bp.route('/coming-soon')
def coming_soon():
    return render_template('coming_soon.html')