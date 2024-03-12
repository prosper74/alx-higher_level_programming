# SQL - Introduction
SQL (Structured Query Language) is a powerful programming language designed for managing and manipulating relational databases. With SQL, users can perform a variety of tasks such as querying data, updating records, defining schema structures, and managing access permissions within a database system. It provides a standardized syntax for interacting with databases, making it widely used across different database management systems (DBMS) like MySQL, PostgreSQL, SQL Server, and Oracle. SQL offers a rich set of commands, including SELECT for retrieving data, INSERT for adding new records, UPDATE for modifying existing data, and DELETE for removing records. Additionally, SQL supports various operations like joins, aggregations, and sorting to efficiently work with large datasets. Overall, SQL serves as the foundation for interacting with relational databases and is essential knowledge for anyone involved in data management, database administration, or software development.

### What’s a database? 
A database is a structured collection of data that is organized and stored electronically. It allows users to easily manage, manipulate, and retrieve data as needed.

### What’s a relational database? 
A relational database is a type of database that organizes data into tables with rows and columns, where each row represents a record and each column represents a specific attribute or field. The relationships between tables are established through keys, usually primary keys and foreign keys.

### What does SQL stand for? 
SQL stands for Structured Query Language. It is a standard programming language used for managing and manipulating relational databases. SQL allows users to perform tasks such as querying data, updating data, creating and modifying database structures, and more.

### What’s MySQL? 
MySQL is an open-source relational database management system (RDBMS) that uses SQL. It is one of the most popular databases in the world and is widely used for web applications, data warehousing, e-commerce, and many other applications.

### How to create a database in MySQL? 
In MySQL, you can create a new database using the `CREATE DATABASE` statement followed by the name of the database. For example:

```
CREATE DATABASE my_database;
```

### What does DDL and DML stand for? 
DDL stands for Data Definition Language, and it is used to define and modify the structure of database objects such as tables, indexes, and views. Examples of DDL statements include CREATE, ALTER, and DROP. DML stands for Data Manipulation Language, and it is used to manipulate data within tables. Examples of DML statements include SELECT, INSERT, UPDATE, and DELETE.

### How to CREATE or ALTER a table? 
To create a new table in MySQL, you use the CREATE TABLE statement followed by the table name and the column definitions. For example:

```
CREATE TABLE my_table (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
```
To alter an existing table, you use the ALTER TABLE statement followed by the table name and the alteration you want to make. For example:

```
ALTER TABLE my_table ADD COLUMN age INT;
```

### How to SELECT data from a table? 
To select data from a table in MySQL, you use the SELECT statement followed by the columns you want to retrieve and the table you want to retrieve them from. For example:

```
SELECT column1, column2 FROM my_table;
```

### How to INSERT, UPDATE or DELETE data? 
To insert new data into a table, you use the INSERT INTO statement followed by the table name and the values you want to insert. For example:

```
INSERT INTO my_table (column1, column2) VALUES (value1, value2);
```

To update existing data in a table, you use the UPDATE statement followed by the table name, the columns you want to update, and the new values. For example:

```
UPDATE my_table SET column1 = value1 WHERE condition;
```

To delete data from a table, you use the DELETE FROM statement followed by the table name and an optional condition. For example:

```
DELETE FROM my_table WHERE condition;
```

### What are subqueries?
Subqueries, also known as nested queries or inner queries, are queries that are embedded within another query. They allow you to retrieve data from one or more tables based on the results of another query. Subqueries can be used in SELECT, INSERT, UPDATE, and DELETE statements.

### How to use MySQL functions?
MySQL provides a wide range of built-in functions that you can use to perform various operations on data. These functions include mathematical functions, string functions, date and time functions, aggregate functions, and more. You can use these functions in your SQL queries to manipulate and transform data as needed.
