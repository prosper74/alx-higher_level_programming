# SQL - More Queries
SQL (Structured Query Language) is a powerful programming language designed for managing and manipulating relational databases. With SQL, users can perform a variety of tasks such as querying data, updating records, defining schema structures, and managing access permissions within a database system. It provides a standardized syntax for interacting with databases, making it widely used across different database management systems (DBMS) like MySQL, PostgreSQL, SQL Server, and Oracle. SQL offers a rich set of commands, including SELECT for retrieving data, INSERT for adding new records, UPDATE for modifying existing data, and DELETE for removing records. Additionally, SQL supports various operations like joins, aggregations, and sorting to efficiently work with large datasets. Overall, SQL serves as the foundation for interacting with relational databases and is essential knowledge for anyone involved in data management, database administration, or software development.

### How to create a new MySQL user?
You can create a new MySQL user using the CREATE USER statement, followed by the username and host from which the user can connect. For example:

```
CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';
```

### How to manage privileges for a user to a database or table? 
You can grant or revoke privileges to a user using the GRANT and REVOKE statements. For example:

```
GRANT SELECT, INSERT ON database.table TO 'username'@'hostname';
REVOKE ALL PRIVILEGES ON database.* FROM 'username'@'hostname';
```

### What’s a PRIMARY KEY?:
A PRIMARY KEY is a column or a set of columns in a table that uniquely identifies each row. It ensures that each row in a table is unique and not null. There can be only one PRIMARY KEY in a table.

### What’s a FOREIGN KEY?:
A FOREIGN KEY is a column or a set of columns in a table that establishes a link between data in two tables. It enforces referential integrity by ensuring that the values in the FOREIGN KEY column(s) match the values in the PRIMARY KEY column(s) of another table.

### How to use NOT NULL and UNIQUE constraints?
You can specify the NOT NULL constraint to enforce that a column cannot contain null values, and the UNIQUE constraint to ensure that all values in a column (or a combination of columns) are unique.

### How to retrieve data from multiple tables in one request?
You can retrieve data from multiple tables in one request using SQL JOINs, which allow you to combine rows from two or more tables based on a related column between them.

### What are subqueries?
Subqueries, also known as nested queries or inner queries, are queries embedded within another query. They allow you to use the result of one query as a part of another query.

### What are JOIN and UNION?
- **JOIN:** JOIN is used to combine rows from two or more tables based on a related column between them. There are different types of JOINs such as `INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN`.

- **UNION:** UNION is used to combine the results of two or more SELECT statements into a single result set. It removes duplicate rows by default unless the UNION ALL operator is used.
