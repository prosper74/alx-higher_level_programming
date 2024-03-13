-- SQL statement retrieves data from the `temperatures` table,
-- calculates the maximum value of the `value` column for each
-- distinct `state`, and then sorts the results based on the `state` column.
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
