-- SQL statement that retrieves data from the 'temperatures' table,
-- calculates the average value of the value column for each distinct city,
-- and then sorts the results based on the average temperature in descending order.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
