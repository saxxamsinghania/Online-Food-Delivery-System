# config.py
import os
import datetime
class Config:
    SECRET_KEY = 'your-secret-key-here'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'password'
    MYSQL_DB = 'online_food_delivery_3'
    MYSQL_CURSORCLASS = 'DictCursor'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/online_food_delivery_3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # # JWT Configuration
    # JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', SECRET_KEY)
    # JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=24)
    # JWT_BLACKLIST_ENABLED = True
    # JWT_BLACKLIST_TOKEN_CHECKS = ['access']

