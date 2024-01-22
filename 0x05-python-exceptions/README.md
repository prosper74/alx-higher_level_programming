# Python - Exceptions 
In Python, errors are generally categorized into two types: syntax errors, which occur during code compilation, and runtime errors, which occur when the code is executed. Exceptions are a type of runtime error that can be handled during program execution.

### What are exceptions and how to use them?
Exceptions in Python are raised when an error occurs during the execution of a program. They can be caught and handled to prevent the program from crashing. You can use the try, except, else, and finally blocks to handle exceptions.

Exceptions are useful when you want to gracefully handle unexpected situations, such as file not found, division by zero, or network errors. They help improve the robustness of your code by allowing you to handle errors in a controlled manner.

To correctly handle an exception, enclose the potentially problematic code within a try block. If an exception occurs, it is caught by the corresponding except block. Optionally, you can use an else block to specify code that should be executed only if no exception occurs. Finally, the finally block is executed regardless of whether an exception occurred or not, making it suitable for cleanup operations.

Here's a simple example:
```
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the specific exception
    print("Cannot divide by zero!")
else:
    # Code to execute if no exception occurred
    print("Division successful.")
finally:
    # Cleanup code (optional)
    print("Finally block executed.")
```

### What’s the purpose of catching exceptions?
Catching exceptions serves the purpose of gracefully handling errors or unexpected situations in your code. Instead of letting the program crash, catching exceptions allows you to provide alternative paths, display meaningful error messages, or perform specific actions to recover from the error. It enhances the robustness of your program by preventing abrupt terminations and allowing for controlled responses to exceptional conditions.

### How to raise a builtin exception? 
You can raise a built-in exception in Python using the raise keyword followed by the exception type. For example:
```
# Raise a ValueError with a custom message
raise ValueError("This is a custom error message")
```

### When do we need to implement a clean-up action after an exception?
Implementing a clean-up action after an exception is crucial when your code involves resources that need to be properly managed, such as closing files, releasing network connections, or cleaning up allocated memory. The finally block is commonly used for such clean-up actions, ensuring that specific code is executed regardless of whether an exception occurred or not.

For example, if you open a file in a try block, you should close it in the finally block to guarantee that the file is closed, even if an exception occurs:
```
try:
    file = open("example.txt", "r")
    # Code that may raise an exception
except FileNotFoundError:
    print("File not found!")
else:
    print("File opened successfully.")
    # Process the file data
finally:
    # Clean-up action: close the file
    file.close()
```

By using the finally block, you ensure that the file is closed regardless of whether the file operations in the try block were successful or not. This helps in maintaining resource integrity and preventing potential issues related to resource leaks.
