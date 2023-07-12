-- 1. To find the ride with the highest and lowest fare from the Rides table in SQL

SELECT * FROM Rides
WHERE fare = (SELECT MAX(fare) FROM Rides)
   OR fare = (SELECT MIN(fare) FROM Rides);


-- 2. To find the average fare and distance for each driver_id from the Rides table in SQL

SELECT driver_id, AVG(fare) AS avg_fare, AVG(distance) AS avg_distance
FROM Rides
GROUP BY driver_id;



-- 3. To find driver_id values that have completed more than 5 rides from the Rides table in SQL

SELECT driver_id, COUNT(*) AS ride_count
FROM Rides
GROUP BY driver_id
HAVING COUNT(*) > 5;



4....


5.


6.


7.


8.


9.


-- 10. To add a tip field to the Rides table in SQL

ALTER TABLE Rides
ADD COLUMN tip DECIMAL(8, 2);



