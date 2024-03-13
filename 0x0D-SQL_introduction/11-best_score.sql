-- Lists all records where score >= 10.
-- Ordered by score in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
