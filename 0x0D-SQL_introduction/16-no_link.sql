-- Lists all records having a 'name' value.
-- Ordered by score in descending.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
