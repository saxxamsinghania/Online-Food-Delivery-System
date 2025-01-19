# Online-Food-Delivery-System

Users can register and login into the food delivery app, select and add to cart their favourite dishes from various restaurants, and then can place the order. The payment of any order can be done by COD(cash on delivery) or through the UPI QR code.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher from the [official website](https://www.python.org/downloads/)
- MySQL 8.0 or higher from the [official website](https://dev.mysql.com/downloads/)
- Git latest version from the [official website](https://git-scm.com/downloads)


---

## Getting Started

### **Clone the Repository**

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/saxxamsinghania/Online-Food-Delivery-System.git
cd Online-Food-Delivery-System/food_delivery_app_v2/
```
---


## Installation

#### **Create a Virtual Environment**

Navigate to the [food_delivery_app_v2](/food_delivery_app_v2) folder and create a virtual environment:

```bash
python -m venv venv        # Command to create a virtual environment named venv
source venv/bin/activate  # Linux/Mac users can use this command to activate the virtual environment 
venv\Scripts\activate     # Windows users can activate the venv using this command
```

Once the virtual environment is activated:

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required modules in the preferred environment.

```bash
pip install -r requirements.txt
```

### **Configuring Database:**

The [config.py](/food_delivery_app_v2/app/config.py) file looks like this:
```python
# config.py

class Config:
    SECRET_KEY = 'your-secret-key-here'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'password'.  #replace here
    MYSQL_DB = 'online_food_delivery_3'
    MYSQL_CURSORCLASS = 'DictCursor'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/online_food_delivery_3' #here replace password
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```
You must replace the 'password' with your actual MySQL root password at the two locations shown with the comments. \
Since, the database is named as online_food_delivery_3, so you have to create a database named 'online_food_delivery_3' using your SQL initially, and migrate it.

Steps to create the required database: 

First we will need to open our MySQL shell: 

For Windows: \
    Open the MySQL-command-client and enter your password. 

For Linux/Mac: \
    Open your terminal then to access your MySQL:
```bash
mysql -u root -p
```
Enter your password and now you are in your MySQL shell. 

Now enter this command to create the required database:
```mysql
CREATE DATABASE online_food_delivery_3;
```

Steps to migrate: \
Using terminal/cmd navigate to the [food_delivery_app_v2](/food_delivery_app_v2) folder and enter following commands:
```bash
flask db init
flask db migrate -m "Initial Migration"
flask db upgrade
```
This will create the required tables and models.

Adding the required sample data to the app:
Navigate to the [Insert_commands.sql](/Insert_commands.sql) file and run it using the MySQL Workbench, this will add all the restaurants and menu to our database.

## Usage

Run [run.py](/food_delivery_app_v2/run.py) to run the app and go to [http://127.0.0.1:5002](http://127.0.0.1:5002) with any browser to interact with the app.
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](./LICENSE)
