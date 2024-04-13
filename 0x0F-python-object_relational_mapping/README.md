# Python - Object-relational mapping

### Python programming is awesome for several reasons:

- Readability: Python's clean and simple syntax makes it easy to read and write code, enhancing developer productivity and reducing the likelihood of errors.
- Versatility: Python can be used for a wide range of applications, including web development, data analysis, machine learning, artificial intelligence, scientific computing, automation, and more.
- Large Standard Library: Python comes with a comprehensive standard library that provides ready-to-use modules and functions for various tasks, reducing the need to reinvent the wheel.
- Community and Ecosystem: Python has a vibrant community of developers who contribute to open-source projects, libraries, and frameworks, enriching the Python ecosystem and providing solutions to diverse problems.
- Cross-platform Compatibility: Python is available on multiple platforms, including Windows, macOS, and Linux, allowing developers to write code that can run seamlessly across different operating systems.

### Connect mysql
To connect to a MySQL database from a Python script, you can use the mysql-connector-python package, which is an official MySQL driver for Python. Here's an example:
```
import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="database_name"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute a SELECT query
cursor.execute("SELECT * FROM table_name")

# Fetch rows from the result set
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
connection.close()
```

### Insert new row
To insert rows into a MySQL table from a Python script, you can use parameterized queries to safely execute SQL statements. Here's an example:
```
# Execute an INSERT query
sql = "INSERT INTO table_name (column1, column2) VALUES (%s, %s)"
values = ("value1", "value2")
cursor.execute(sql, values)

# Commit the transaction
connection.commit()
```

### What is ORM
ORM stands for Object-Relational Mapping. It's a programming technique for converting data between incompatible systems, such as object-oriented programming languages and relational databases. ORMs map objects from the application code to tables in the database, providing a higher-level abstraction and making it easier to interact with the database using object-oriented concepts.

### Map Python class to table
To map a Python class to a MySQL table using an ORM like SQLAlchemy, you would define a class that represents the table structure and relationships, and then use SQLAlchemy's declarative base to create a mapping between the class and the table. Here's a simplified example:
```
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create engine and create tables
engine = create_engine('mysql+mysqlconnector://username:password@localhost/database_name')
Base.metadata.create_all(engine)
```

### Python virtual environment
To create a Python virtual environment, you can use the venv module, which is included in Python 3. It allows you to create isolated environments for Python projects, ensuring that dependencies are kept separate and preventing conflicts between different projects.

Here's how you can create a virtual environment:
- Open a terminal or command prompt.
- Navigate to the directory where you want to create the virtual environment.
- Run the following command:
```
python3 -m venv myenv
```

This command creates a new directory named myenv, which contains the virtual environment. You can replace myenv with any name you prefer.

pip3 install python3-dev libmysqlclient-dev zlib1g-dev mysqlclient
