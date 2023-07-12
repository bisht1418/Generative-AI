-- 1. To create a Rides table in SQL

CREATE TABLE Rides (
  id INT PRIMARY KEY,
  start_location VARCHAR(255),
  end_location VARCHAR(255),
  distance DECIMAL(5, 2),
  fare DECIMAL(8, 2),
  ride_time INT,
  driver_id INT
);


-- 2. To insert data into the Rides table in SQL

INSERT INTO Rides (id, start_location, end_location, distance, fare, ride_time, driver_id)
VALUES
  (1, 'Location A', 'Location B', 10.5, 25.75, 30, 1),
  (2, 'Location C', 'Location D', 8.2, 20.50, 25, 2),
  (3, 'Location E', 'Location F', 5.3, 15.25, 20, 3),
  (4, 'Location G', 'Location H', 12.1, 30.00, 35, 1),
  (5, 'Location I', 'Location J', 7.6, 18.75, 22, 2);


-- 3. To fetch all rides ordered by fare in descending order from the Rides table in SQL

SELECT * FROM Rides ORDER BY fare DESC;


-- 4. To calculate the total distance and total fare for all rides in the Rides table in SQL

SELECT SUM(distance) AS total_distance, SUM(fare) AS total_fare FROM Rides;


-- 5. To calculate the average ride_time of all rides in the Rides table in SQL

SELECT AVG(ride_time) FROM Rides;



-- 6. To fetch all rides whose start_location or end_location contains 'Downtown' from the Rides table in SQL

SELECT * FROM Rides WHERE start_location LIKE '%Downtown%' OR end_location LIKE '%Downtown%';


-- 7. To count the number of rides for a given driver_id from the Rides table in SQL

SELECT COUNT(*) FROM Rides WHERE driver_id = 2;


-- 8. To update the fare of the ride with id 4 in the Rides table in SQL

UPDATE Rides SET fare = 35.50 WHERE id = 4;



-- 9. To calculate the total fare for each driver_id from the Rides table in SQL

SELECT driver_id, SUM(fare) AS total_fare FROM Rides GROUP BY driver_id;



-- 10. To delete the ride with id 2 from the Rides table in SQL

DELETE FROM Rides WHERE id = 2;
