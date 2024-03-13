-- SQL statement performs an alteration on the 'first_table'
-- in the 'hbtn_0c_0' database, converting its character set
-- to 'utf8mb4' and its collation to 'utf8mb4_unicode_ci'
-- Reason: This alteration allows the table to store and
-- handle a wider range of characters and ensures proper
-- sorting and comparison of Unicode data.
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
