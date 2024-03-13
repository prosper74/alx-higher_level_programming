-- Lists the number of records with the same score.
-- The result will display:
-- -- the score
-- -- the number of records for this score with the label number
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
