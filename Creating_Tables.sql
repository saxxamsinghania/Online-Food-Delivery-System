CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    PhoneNumber VARCHAR(15),
    Address VARCHAR(255),
    Password VARCHAR(100)
);

CREATE TABLE Restaurant (
    RestaurantID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Location VARCHAR(255),
    ContactNumber VARCHAR(15),
    CuisineType VARCHAR(100),
    Rating DECIMAL(3, 2) DEFAULT 0.00
);

CREATE TABLE MenuItem (
    MenuItemID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Price DECIMAL(10, 2),
    Description TEXT,
    Category VARCHAR(100),
    Rating DECIMAL(3, 2) DEFAULT 0.00,
    RestaurantID INT,
    FOREIGN KEY (RestaurantID) REFERENCES Restaurant(RestaurantID) ON DELETE CASCADE
);

CREATE TABLE `Order` (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    TotalAmount DECIMAL(10, 2),
    Status VARCHAR(50),
    TimeToReach TIME,
    Rating DECIMAL(3, 2) DEFAULT 0.00,
    CustomerID INT,
    RestaurantID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (RestaurantID) REFERENCES Restaurant(RestaurantID) ON DELETE CASCADE
);

CREATE TABLE OrderItem (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,
    Quantity INT,
    Price DECIMAL(10, 2),
    MenuItemID INT,
    OrderID INT,
    FOREIGN KEY (MenuItemID) REFERENCES MenuItem(MenuItemID) ON DELETE CASCADE,
    FOREIGN KEY (OrderID) REFERENCES `Order`(OrderID) ON DELETE CASCADE
);

CREATE TABLE DeliveryPerson (
    DeliveryPersonID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    PhoneNumber VARCHAR(15),
    VehicleDetails VARCHAR(100),
    Rating DECIMAL(3, 2) DEFAULT 0.00
);

CREATE TABLE Payment (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,
    PaymentDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    PaymentMethod VARCHAR(50),
    PaymentStatus VARCHAR(50),
    Amount DECIMAL(10, 2),
    OrderID INT,
    FOREIGN KEY (OrderID) REFERENCES `Order`(OrderID) ON DELETE CASCADE
);
