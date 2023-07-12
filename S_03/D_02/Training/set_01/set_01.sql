
-- 1. To create a Customers table in SQL

CREATE TABLE Customers (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  address VARCHAR(255),
  phone_number VARCHAR(20)
);


-- 2. To insert data into the Customers table in SQL

INSERT INTO Customers (id, name, email, address, phone_number)
VALUES
  (1, 'Neeraj', 'neeraj@gmail.com', '123 Main St', '8920086184'),
  (2, 'Jarnee', 'jarnee@gmail.com', 'uttarakhand', '1414141414'),


-- 3. To fetch all data from the Customers table in SQL

SELECT * FROM Customers;


-- 4. To select only the name and email fields for all customers in SQL

SELECT name, email FROM Customers;


-- 5. To fetch the customer with the id of 3 from the Customers

SELECT * FROM Customers WHERE id = 3;


-- 6. To fetch all customers whose name starts with 'A' from the Customers table in SQL

SELECT * FROM Customers WHERE name LIKE 'A%';


-- 7. To fetch all customers ordered by name in descending order from the Customers table in SQL

SELECT * FROM Customers ORDER BY name DESC;


-- 8. To update the address of the customer with id 4 in the Customers table in SQL


UPDATE Customers SET address = 'New Address' WHERE id = 2;


-- 9. To fetch the top 3 customers when ordered by id in ascending order from the Customers table in SQL

SELECT * FROM Customers ORDER BY id ASC LIMIT 3;


-- 10. To delete the customer with id 2 from the Customers table in SQL

DELETE FROM Customers WHERE id = 2;


-- 11. To count the number of customers in the Customers table in SQL

SELECT COUNT(*) FROM Customers;


-- 12. To fetch all customers except the first two when ordered by id in ascending order from the Customers table in SQL

SELECT * FROM Customers ORDER BY id ASC OFFSET 2;


-- 13. To fetch all customers whose id is greater than 2 and name starts with 'B' from the Customers table in SQL

SELECT * FROM Customers WHERE id > 2 AND name LIKE 'B%';


-- 14. To fetch all customers whose id is less than 3 or name ends with 's' from the Customers table in SQL

SELECT * FROM Customers WHERE id < 3 OR name LIKE '%s';


-- 15. To fetch all customers where the phone_number field is not set or is null from the Customers table in SQ

SELECT * FROM Customers WHERE phone_number IS NULL OR phone_number = '';
