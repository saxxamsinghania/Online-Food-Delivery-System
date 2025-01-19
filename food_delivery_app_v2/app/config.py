# config.py

class Config:
    SECRET_KEY = 'your-secret-key-here'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'password'        #replace here with your password
    MYSQL_DB = 'online_food_delivery_3'
    MYSQL_CURSORCLASS = 'DictCursor'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/online_food_delivery_3'    #here in place of password
    SQLALCHEMY_TRACK_MODIFICATIONS = False
