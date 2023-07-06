-- **Problem 1:**
CREATE TABLE Customers (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  email VARCHAR(255),
  address VARCHAR(255),
  phone_number VARCHAR(20)
);


-- Answer_02
INSERT INTO Customers (name, email, address, phone_number)
VALUES
  ('John Doe', 'john.doe@example.com', '123 Main St', '1234567890'),
  ('Jane Smith', 'jane.smith@example.com', '456 Elm St', '9876543210'),
  ('Mike Johnson', 'mike.johnson@example.com', '789 Oak Ave', '5555555555'),
  ('Sarah Williams', 'sarah.williams@example.com', '321 Pine St', '7777777777'),
  ('David Brown', 'david.brown@example.com', '654 Cedar Rd', '1111111111');



-- Answer_03
SELECT * FROM Customers;


-- Answer_04
SELECT name, email FROM Customers;


-- Answer_05
SELECT * FROM Customers WHERE id = 3;


-- Answer_06
SELECT * FROM Customers WHERE name LIKE 'A%';


-- Answer_07
SELECT * FROM Customers ORDER BY name DESC;


-- Answer_08
UPDATE Customers SET address = 'New Address' WHERE id = 4;


-- Answer_09
SELECT * FROM Customers ORDER BY id ASC LIMIT 3;


-- Answer_10
DELETE FROM Customers WHERE id = 2;


-- Answer_11
SELECT COUNT(*) AS total_customers FROM Customers;


-- Answewr_12
SELECT * FROM Customers ORDER BY id ASC LIMIT 18446744073709551615 OFFSET 2;


-- Answer_13
SELECT * FROM Customers WHERE id > 2 AND name LIKE 'B%';


-- Answer_14
SELECT * FROM Customers WHERE id < 3 OR name LIKE '%s';


-- Answer_15
SELECT * FROM Customers WHERE phone_number IS NULL OR phone_number = '';






