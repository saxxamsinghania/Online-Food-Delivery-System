INSERT INTO restaurant (Name, Location, ContactNumber, CuisineType, Rating) VALUES
('Bella Italia', '123 Main St, Mumbai, Maharashtra', '9876543210', 'Italian', 4.5),
('Sushi Sensation', '456 Ocean Ave, Bengaluru, Karnataka', '9876543211', 'Japanese', 4.7),
('Taco Fiesta', '789 Broadway, Pune, Maharashtra', '9876543212', 'Mexican', 4.3),
('Green Leaf Bistro', '234 Elm St, Hyderabad, Telangana', '9876543213', 'Vegetarian', 4.6),
('Spice Route', '567 King St, Delhi', '9876543214', 'Indian', 4.4),
('Burger Haven', '890 Park Ave, Kolkata, West Bengal', '9876543215', 'American', 4.2),
('Noodle House', '345 Rice St, Chennai, Tamil Nadu', '9876543216', 'Chinese', 4.5),
('Mediterranean Delight', '678 Olive St, Ahmedabad, Gujarat', '9876543217', 'Mediterranean', 4.6),
('BBQ Pit', '901 Smokey Rd, Jaipur, Rajasthan', '9876543218', 'BBQ', 4.8),
('Pho Paradise', '234 Saigon St, Lucknow, Uttar Pradesh', '9876543219', 'Vietnamese', 4.4),
('French Connection', '567 Champs St, Chandigarh', '9876543220', 'French', 4.5),
('Curry Corner', '890 Spice Blvd, Bhopal, Madhya Pradesh', '9876543221', 'Indian', 4.3),
('Pizza Palace', '123 Slice St, Nagpur, Maharashtra', '9876543222', 'Italian', 4.6),
('Seafood Shack', '456 Harbor Rd, Kochi, Kerala', '9876543223', 'Seafood', 4.7),
('Vegan Vibes', '789 Green St, Goa', '9876543224', 'Vegan', 4.5),
('Grill Master', '234 Flame Ave, Amritsar, Punjab', '9876543225', 'Steakhouse', 4.4),
('Ramen Republic', '567 Noodle Ln, Coimbatore, Tamil Nadu', '9876543226', 'Japanese', 4.6),
('Tex-Mex Express', '890 Salsa St, Indore, Madhya Pradesh', '9876543227', 'Tex-Mex', 4.3),
('Soul Food Kitchen', '123 Soul St, Surat, Gujarat', '9876543228', 'Southern', 4.5),
('Dim Sum Palace', '456 Dragon St, Vadodara, Gujarat', '9876543229', 'Chinese', 4.7);

-- Insert Menu Items for Each Restaurant in Rupees
-- Bella Italia
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Margherita Pizza', 999, 'Classic pizza with tomato sauce, mozzarella, and basil', 'Pizza', 4.5, 1),
('Spaghetti Carbonara', 1149, 'Creamy pasta with pancetta and parmesan', 'Pasta', 4.6, 1),
('Tiramisu', 619, 'Traditional Italian dessert with coffee and mascarpone', 'Dessert', 4.7, 1),
('Caprese Salad', 769, 'Fresh mozzarella, tomatoes, and basil', 'Appetizer', 4.5, 1);

-- Sushi Sensation
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Dragon Roll', 1309, 'Eel and cucumber roll topped with avocado', 'Sushi', 4.8, 2),
('Sashimi Platter', 1929, 'Chef''s selection of fresh raw fish', 'Sashimi', 4.7, 2),
('Miso Soup', 459, 'Traditional Japanese soup', 'Soup', 4.5, 2),
('Green Tea Ice Cream', 539, 'Refreshing green tea flavored dessert', 'Dessert', 4.6, 2);

-- Taco Fiesta
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Carnitas Tacos', 929, 'Slow-cooked pulled pork tacos', 'Tacos', 4.6, 3),
('Guacamole', 619, 'Fresh made guacamole with chips', 'Appetizer', 4.7, 3),
('Chicken Enchiladas', 1079, 'Corn tortillas filled with chicken and cheese', 'Entree', 4.5, 3),
('Churros', 539, 'Traditional Mexican dessert', 'Dessert', 4.6, 3);

-- Green Leaf Bistro
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Quinoa Buddha Bowl', 1159, 'Roasted vegetables over quinoa with tahini dressing', 'Bowl', 4.7, 4),
('Vegan Burger', 999, 'Plant-based patty with all the fixings', 'Burger', 4.6, 4),
('Kale Caesar Salad', 849, 'Vegan caesar salad with homemade croutons', 'Salad', 4.5, 4),
('Chia Seed Pudding', 619, 'Coconut milk chia pudding with fresh berries', 'Dessert', 4.6, 4);

-- Spice Route
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Chicken Tikka Masala', 1229, 'Classic Indian curry with tender chicken', 'Curry', 4.6, 5),
('Vegetable Samosas', 689, 'Crispy pastry filled with spiced vegetables', 'Appetizer', 4.5, 5),
('Garlic Naan', 389, 'Traditional Indian flatbread', 'Bread', 4.7, 5),
('Mango Lassi', 459, 'Refreshing yogurt drink', 'Beverage', 4.6, 5);

-- Burger Haven
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Classic Cheeseburger', 929, 'Beef patty with cheese, lettuce, and tomato', 'Burger', 4.5, 6),
('Loaded Fries', 689, 'Fries topped with cheese, bacon, and green onions', 'Side', 4.6, 6),
('Milkshake', 539, 'Thick and creamy classic milkshake', 'Dessert', 4.7, 6),
('Chicken Wings', 999, 'Spicy buffalo chicken wings', 'Appetizer', 4.5, 6);

-- Noodle House
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Vegetable Chow Mein', 789, 'Stir-fried noodles with mixed vegetables', 'Noodles', 4.5, 7),
('Kung Pao Chicken', 1149, 'Spicy chicken with peanuts and vegetables', 'Main Course', 4.6, 7),
('Spring Rolls', 459, 'Crispy vegetable spring rolls', 'Appetizer', 4.5, 7),
('Egg Fried Rice', 689, 'Classic Chinese fried rice with eggs', 'Rice', 4.4, 7);

-- Mediterranean Delight
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Hummus Platter', 769, 'Traditional hummus with pita bread', 'Appetizer', 4.6, 8),
('Lamb Shawarma', 1309, 'Slow-roasted lamb in traditional spices', 'Main Course', 4.7, 8),
('Greek Salad', 619, 'Fresh salad with feta and olives', 'Salad', 4.5, 8),
('Baklava', 459, 'Sweet pastry with nuts and honey', 'Dessert', 4.6, 8);

-- BBQ Pit
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Pulled Pork Platter', 1229, 'Slow-cooked pulled pork with BBQ sauce', 'BBQ', 4.8, 9),
('Beef Brisket', 1399, 'Smoky beef brisket with house rub', 'Main Course', 4.7, 9),
('Corn Bread', 389, 'Traditional southern corn bread', 'Side', 4.5, 9),
('Apple Pie', 539, 'Classic American apple pie', 'Dessert', 4.6, 9);

-- Pho Paradise
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Classic Beef Pho', 689, 'Traditional Vietnamese noodle soup', 'Soup', 4.5, 10),
('Spring Roll Platter', 539, 'Fresh and crispy Vietnamese spring rolls', 'Appetizer', 4.6, 10),
('Chicken Banh Mi', 769, 'Vietnamese sandwich with grilled chicken', 'Sandwich', 4.5, 10),
('Vietnamese Coffee', 299, 'Strong coffee with condensed milk', 'Beverage', 4.4, 10);

-- French Connection
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Coq au Vin', 1399, 'Classic French chicken braised in wine', 'Main Course', 4.6, 11),
('French Onion Soup', 619, 'Traditional cheese-topped onion soup', 'Soup', 4.5, 11),
('Crème Brûlée', 539, 'Classic French custard dessert', 'Dessert', 4.7, 11),
('Cheese Platter', 999, 'Selection of French cheeses', 'Appetizer', 4.5, 11);

-- Curry Corner
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Butter Chicken', 1149, 'Creamy tomato-based chicken curry', 'Curry', 4.6, 12),
('Palak Paneer', 929, 'Spinach and cottage cheese curry', 'Vegetarian', 4.5, 12),
('Jeera Rice', 389, 'Fragrant cumin rice', 'Side', 4.4, 12),
('Gulab Jamun', 299, 'Sweet milk-solid balls in sugar syrup', 'Dessert', 4.6, 12);

-- Pizza Palace
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Quattro Formaggi Pizza', 1079, 'Four cheese pizza', 'Pizza', 4.7, 13),
('Pepperoni Italiano', 1229, 'Classic pepperoni pizza', 'Pizza', 4.6, 13),
('Caesar Salad', 619, 'Traditional Caesar salad', 'Salad', 4.5, 13),
('Tiramisu Classico', 539, 'Classic Italian tiramisu', 'Dessert', 4.6, 13);

-- Seafood Shack
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Grilled Fish Thali', 1309, 'Assorted seafood platter', 'Seafood', 4.7, 14),
('Prawn Masala', 1229, 'Spicy prawn curry', 'Curry', 4.6, 14),
('Fish Tikka', 999, 'Tandoori style fish tikka', 'Appetizer', 4.5, 14),
('Coconut Pudding', 459, 'Creamy coconut dessert', 'Dessert', 4.6, 14);

-- Vegan Vibes
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Tofu Scramble', 769, 'Spiced tofu breakfast scramble', 'Breakfast', 4.6, 15),
('Vegan Thali', 1149, 'Complete vegan meal platter', 'Main Course', 4.7, 15),
('Avocado Toast', 619, 'Artisan bread with avocado spread', 'Appetizer', 4.5, 15),
('Raw Chocolate Cake', 539, 'Vegan raw chocolate dessert', 'Dessert', 4.6, 15);

-- Grill Master
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Tenderloin Steak', 1929, 'Premium beef tenderloin', 'Steak', 4.7, 16),
('Lamb Chops', 1399, 'Grilled herb-marinated lamb chops', 'Main Course', 4.6, 16),
('Mashed Potatoes', 389, 'Creamy butter mashed potatoes', 'Side', 4.5, 16),
('Chocolate Lava Cake', 619, 'Warm chocolate lava cake', 'Dessert', 4.6, 16);

-- Ramen Republic
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Tonkotsu Ramen', 929, 'Rich pork bone broth ramen', 'Ramen', 4.7, 17),
('Gyoza Platter', 689, 'Pan-fried Japanese dumplings', 'Appetizer', 4.6, 17),
('Edamame', 299, 'Steamed and salted soybean pods', 'Side', 4.5, 17),
('Matcha Ice Cream', 459, 'Traditional green tea ice cream', 'Dessert', 4.6, 17);

-- Tex-Mex Express
INSERT INTO menu_item (Name, Price, Description, Category, Rating, RestaurantID) VALUES
('Beef Fajitas', 1149, 'Sizzling beef fajitas with tortillas', 'Main Course', 4.6, 18),
('Queso Fundido', 769, 'Melted cheese with chorizo', 'Appetizer', 4.5, 18),
('Chimichanga', 999, 'Deep-fried stuffed burrito', '
