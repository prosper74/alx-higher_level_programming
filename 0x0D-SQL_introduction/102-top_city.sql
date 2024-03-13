-- SQL statement retrieves data from the `temperatures` table,
-- calculates the average value of the `value` column for each
-- distinct city where the month column is July and August (7 or 8),
-- and then sorts the results based on the average temperature
-- in descending order. The result is limited to the top 3
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
