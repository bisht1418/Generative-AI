-- 16. To create a Restaurants table in SQL

CREATE TABLE Restaurants (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  location VARCHAR(255),
  cuisine_type VARCHAR(255),
  average_rating DECIMAL(3, 2),
  delivery_available BOOLEAN
);


-- 17. To insert data into the Restaurants table in SQL

INSERT INTO Restaurants (id, name, location, cuisine_type, average_rating, delivery_available)
VALUES
  (1, 'Restaurant A', 'New Delhi', 'Italian', 4.5, true),
  (2, 'Restaurant B', 'Pauri', 'Mexican', 4.2, false),
  (3, 'Restaurant C', 'Almora', 'Steakhouse', 4.7, true),
  (4, 'Restaurant D', 'Kedarnath', 'Japanese', 4.4, true),
  (5, 'Restaurant E', 'Manali', 'Seafood', 4.9, true);



-- 18. To fetch all restaurants ordered by average_rating in descending order from the Restaurants table in SQL 

SELECT * FROM Restaurants ORDER BY average_rating DESC;



-- 19. To fetch all restaurants that offer delivery_available and have an average_rating of more than 4 from the Restaurants table in SQL

SELECT * FROM Restaurants WHERE delivery_available = true AND average_rating > 4;



-- 20. To fetch all restaurants where the cuisine_type field is not set or is null from the Restaurants table in SQL 

SELECT * FROM Restaurants WHERE cuisine_type IS NULL OR cuisine_type = '';




-- 21. To count the number of restaurants that have delivery_available from the Restaurants table in SQL

SELECT COUNT(*) FROM Restaurants WHERE delivery_available = true;




-- 22.To fetch all restaurants whose location contains 'New York' from the Restaurants table in SQ

SELECT * FROM Restaurants WHERE location LIKE '%New Delhi%';



-- 23. To calculate the average average_rating of all restaurants in the Restaurants table in SQL


SELECT AVG(average_rating) FROM Restaurants;



-- 24. To fetch the top 5 restaurants when ordered by average_rating in descending order from the Restaurants table in SQL

SELECT * FROM Restaurants ORDER BY average_rating DESC LIMIT 5;



-- 25. To delete the restaurant with id 3 from the Restaurants table in SQL

DELETE FROM Restaurants WHERE id = 3;