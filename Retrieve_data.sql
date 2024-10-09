-- 1. Retrieve all customers
SELECT * FROM Customer;

-- 2. Retrieve all restaurants and their ratings
SELECT Name, Location, CuisineType, Rating
FROM Restaurant;

-- 3. List all menu items offered by a specific restaurant (e.g., RestaurantID = 1)
SELECT Name, Price, Description, Rating
FROM MenuItem
WHERE RestaurantID = 1;

-- 4. Retrieve orders placed by a specific customer (e.g., CustomerID = 1)
SELECT OrderID, OrderDate, TotalAmount, Status, TimeToReach, Rating
FROM `Order`
WHERE CustomerID = 1;

-- 5. Retrieve all menu items in a specific order (e.g., OrderID = 1)
SELECT MenuItem.Name, OrderItem.Quantity, OrderItem.Price
FROM OrderItem
JOIN MenuItem ON OrderItem.MenuItemID = MenuItem.MenuItemID
WHERE OrderItem.OrderID = 1;

-- 6. Retrieve all completed orders with their payment status
SELECT o.OrderID, o.OrderDate, o.TotalAmount, p.PaymentMethod, p.PaymentStatus
FROM `Order` o
JOIN Payment p ON o.OrderID = p.OrderID
WHERE p.PaymentStatus = 'Completed';

-- 7. List all delivery persons and their average ratings
SELECT DeliveryPersonID, Name, PhoneNumber, VehicleDetails, Rating
FROM DeliveryPerson;

-- 8. Retrieve all orders delivered by a specific delivery person (e.g., DeliveryPersonID = 1)
-- (Assumes a relation exists between DeliveryPerson and Order tables)
SELECT o.OrderID, o.OrderDate, o.TotalAmount, o.Status
FROM `Order` o
JOIN DeliveryPerson dp ON dp.DeliveryPersonID = o.OrderID -- This relation needs to be specified
WHERE dp.DeliveryPersonID = 1;

-- 9. Retrieve average rating for a specific menu item (e.g., MenuItemID = 1)
SELECT Name, AVG(Rating) AS AverageRating
FROM MenuItem
WHERE MenuItemID = 1;

-- 10. Retrieve all orders with a total amount greater than $20
SELECT OrderID, CustomerID, TotalAmount, Status
FROM `Order`
WHERE TotalAmount > 20;

-- 11. List all restaurants with average ratings above 4.0
SELECT Name, Location, Rating
FROM Restaurant
WHERE Rating > 4.0;

-- 12. Find total sales (sum of all orders) for a specific restaurant (e.g., RestaurantID = 1)
SELECT SUM(TotalAmount) AS TotalSales
FROM `Order`
WHERE RestaurantID = 1;

-- 13. Retrieve all payments made via credit card
SELECT PaymentID, PaymentMethod, Amount, PaymentStatus
FROM Payment
WHERE PaymentMethod = 'Credit Card';

-- 14. Get the average delivery time for all orders
SELECT AVG(TIMESTAMPDIFF(MINUTE, OrderDate, OrderDate + INTERVAL TIME_TO_SEC(TimeToReach) SECOND)) AS AvgDeliveryTime
FROM `Order`;
