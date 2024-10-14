-- 1. Update the status of an order when it is delivered
UPDATE `Order`
SET Status = 'Delivered'
WHERE OrderID = 1;

-- 2. Update customer address when they move to a new location
UPDATE Customer
SET Address = '789 New Avenue'
WHERE CustomerID = 1;

-- 3. Update restaurant rating based on customer feedback
UPDATE Restaurant
SET Rating = (Rating + 4.8) / 2  -- Assume a customer gives a new rating of 4.8
WHERE RestaurantID = 1;

-- 4. Cancel an order and adjust stock (if needed)
UPDATE `Order`
SET Status = 'Cancelled'
WHERE OrderID = 2;

-- Optionally, remove items from the order or adjust stock
DELETE FROM OrderItem WHERE OrderID = 2;

-- 5. Update the delivery person's rating after a completed order
UPDATE DeliveryPerson
SET Rating = (Rating + 4.5) / 2  -- Assume a new customer rating of 4.5
WHERE DeliveryPersonID = 1;

-- 6. Modify a menu item’s price due to inflation or a promotion
-- Increase price by 10%
UPDATE MenuItem
SET Price = Price * 1.10
WHERE MenuItemID = 1;

-- Apply a 10% discount for promotion
UPDATE MenuItem
SET Price = Price * 0.90
WHERE MenuItemID = 2;

-- 7. Delete an order that was wrongly placed or for test purposes
DELETE FROM `Order`
WHERE OrderID = 3;

-- 8. Update the payment status after successful completion
UPDATE Payment
SET PaymentStatus = 'Completed'
WHERE PaymentID = 1;

-- 9. Add a new item to an existing order (e.g., customer adds fries)
INSERT INTO OrderItem (Quantity, Price, MenuItemID, OrderID)
VALUES (1, 3.49, 4, 1);  -- Fries added to Order 1

-- 10. Refund an order and adjust the payment after a customer complaint
-- Update the order status to "Refunded"
UPDATE `Order`
SET Status = 'Refunded'
WHERE OrderID = 2;

-- Update the payment status and amount
UPDATE Payment
SET PaymentStatus = 'Refunded', Amount = 0.00
WHERE OrderID = 2;

-- 11. Change a customer's phone number after they update their contact info
UPDATE Customer
SET PhoneNumber = '9876543210'
WHERE CustomerID = 2;

-- 12. Increase delivery time due to unexpected delays (e.g., traffic)
UPDATE `Order`
SET TimeToReach = '01:00:00'  -- New estimated time of 1 hour
WHERE OrderID = 1;

-- 13. Change the cuisine type of a restaurant (e.g., if they shift focus)
UPDATE Restaurant
SET CuisineType = 'Mediterranean'
WHERE RestaurantID = 1;

-- 14. Update an order's total amount due to additional charges (e.g., delivery fees)
UPDATE `Order`
SET TotalAmount = TotalAmount + 2.50  -- Adding delivery fee or extra items
WHERE OrderID = 1;

-- 15. Remove a menu item that is no longer available (e.g., out of stock or discontinued)
DELETE FROM MenuItem
WHERE MenuItemID = 3;
