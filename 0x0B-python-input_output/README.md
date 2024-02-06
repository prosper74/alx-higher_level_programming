# Python - Input/Output
This README provides an overview of input/output operations in Python, including reading from and writing to files, handling user input, and using standard input/output functions. Learn how to open, read, and write files, as well as how to interact with users through input prompts and output displays. Explore the flexibility and simplicity of Python's input/output capabilities for various applications.

### How to open a file?
You can open a file in Python using the open() function. For example:
```
file = open("filename.txt", "r")  # Opens the file in read mode
```

### How to write text in a file?
After opening the file in write mode ("w"), you can use the write() method to write text to the file. For example:
```
file = open("filename.txt", "w")
file.write("Hello, world!")
```

### How to read the full content of a file?
After opening the file in read mode ("r"), you can use the read() method to read the full content of the file into a string. For example:
```
file = open("filename.txt", "r")
content = file.read()
```

### How to read a file line by line?
After opening the file in read mode ("r"), you can use a for loop to iterate over each line in the file. For example:
```
file = open("filename.txt", "r")
for line in file:
    print(line)
```

### How to move the cursor in a file?
You can move the cursor in a file using the seek() method. For example:
```
file = open("filename.txt", "r")
file.seek(10)  # Moves the cursor to the 10th byte in the file
```

### How to make sure a file is closed after using it?
You can ensure that a file is closed after using it by explicitly calling the close() method on the file object. For example:
```
file = open("filename.txt", "r")
# Do something with the file
file.close()
```

### What is and how to use the 'with' statement?
The `with` statement in Python is used to ensure that a resource is properly managed and cleaned up, even if an exception occurs. It is commonly used with file operations to automatically close the file after using it. For example:
```
with open("filename.txt", "r") as file:
    content = file.read()
```

### What is JSON?
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is commonly used for transmitting data between a server and a web application.

### What is serialization?
Serialization is the process of converting a Python data structure into a format that can be stored or transmitted and later reconstructed into the original data structure.

### What is deserialization?
Deserialization is the process of converting a serialized data format back into a Python data structure.

### How to convert a Python data structure to a JSON string?
You can use the json.dumps() function to convert a Python data structure to a JSON string. For example:
```
import json
data = {"name": "John", "age": 30}
json_string = json.dumps(data)
```

### How to convert a JSON string to a Python data structure?
You can use the json.loads() function to convert a JSON string to a Python data structure. For example:
```
import json
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
```
