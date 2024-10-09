INSERT INTO Customer (Name, Email, PhoneNumber, Address, Password)
VALUES
('John Doe', 'john.doe@example.com', '1234567890', '123 Main St', 'password123'),
('Jane Smith', 'jane.smith@example.com', '0987654321', '456 Elm St', 'password456');

INSERT INTO Restaurant (Name, Location, ContactNumber, CuisineType, Rating)
VALUES
('Pasta Palace', '789 King St', '1112223333', 'Italian', 4.5),
('Burger Barn', '123 Queen St', '4445556666', 'American', 4.0);

INSERT INTO MenuItem (Name, Price, Description, Category, Rating, RestaurantID)
VALUES
('Spaghetti Carbonara', 12.99, 'Creamy pasta with bacon and egg', 'Main Course', 4.7, 1),
('Margherita Pizza', 9.99, 'Classic pizza with tomato, basil, and mozzarella', 'Main Course', 4.6, 1),
('Cheeseburger', 8.99, 'Beef patty with cheese, lettuce, and tomato', 'Main Course', 4.3, 2),
('Fries', 3.49, 'Crispy golden fries', 'Side', 4.1, 2);

INSERT INTO `Order` (TotalAmount, Status, TimeToReach, Rating, CustomerID, RestaurantID)
VALUES
(26.98, 'Delivered', '00:45:00', 4.8, 1, 1),
(12.48, 'Delivered', '00:30:00', 4.5, 2, 2);

INSERT INTO OrderItem (Quantity, Price, MenuItemID, OrderID)
VALUES
(1, 12.99, 1, 1),
(1, 9.99, 2, 1),
(1, 8.99, 3, 2),
(1, 3.49, 4, 2);

INSERT INTO DeliveryPerson (Name, PhoneNumber, VehicleDetails, Rating)
VALUES
('Mike Johnson', '5556667777', 'Bike - Red', 4.9),
('Emily Davis', '7778889999', 'Scooter - Blue', 4.6);

INSERT INTO Payment (PaymentMethod, PaymentStatus, Amount, OrderID)
VALUES
('Credit Card', 'Completed', 26.98, 1),
('Cash', 'Completed', 12.48, 2);
