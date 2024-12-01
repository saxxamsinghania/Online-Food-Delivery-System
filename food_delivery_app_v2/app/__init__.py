# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mysqldb import MySQL
from flask_migrate import Migrate
# from flask_jwt_extended import JWTManager
from .config import Config

mysql = MySQL()

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
# jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # mysql = MySQL(app)
    mysql.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    # jwt.init_app(app)
    
    from .routes import auth, customer, restaurant, order, home
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(customer.bp)
    app.register_blueprint(restaurant.bp)
    app.register_blueprint(order.bp)

    return app