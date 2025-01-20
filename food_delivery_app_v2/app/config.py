# config.py
class Config:
    SECRET_KEY = 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/online_food_delivery'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
