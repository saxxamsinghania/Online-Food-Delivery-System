# app/routes/auth.py
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Customer
from app import mysql

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone_number = request.form['phone_number']
        address = request.form['address']
        
        cur = mysql.connection.cursor()
        
        cur.execute('SELECT * FROM Customer WHERE Email = %s', (email,))
        if cur.fetchone():
            flash('Email already registered')
            return redirect(url_for('auth.register'))
        
        cur.execute(
            'INSERT INTO Customer (Name, Email, Password, PhoneNumber, Address) VALUES (%s, %s, %s, %s, %s)',
            (name, email, generate_password_hash(password), phone_number, address)
        )
        mysql.connection.commit()
        cur.close()
        
        flash('Registration successful')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = Customer.get_by_email(email)
        if user and check_password_hash(user.Password, password):
            login_user(user)
            return redirect(url_for('customer.dashboard'))
        
        flash('Invalid email or password')
    
    return render_template('auth/login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
