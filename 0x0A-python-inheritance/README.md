# Python - Inheritance
This project explores the concept of inheritance in Python. Inheritance allows the creation of new classes by inheriting attributes and methods from existing classes. The README provides insights into superclass, subclass relationships, overriding methods, multiple inheritance, and the use of built-in functions like isinstance, issubclass, type, and super. Explore the power of code reuse and structuring through the inheritance mechanism in Python.

### What is a superclass, base class, or parent class?
A superclass, base class, or parent class is a class that is extended or inherited by another class called a subclass.

### What is a subclass?
A subclass is a class that inherits attributes and methods from a superclass or base class. It can also have additional attributes or methods.

### How to list all attributes and methods of a class or instance?
You can use the dir() function to get a list of attributes and methods.

### When can an instance have new attributes?
An instance can have new attributes assigned to it at any time.

### How to inherit class from another?
Inheritance is achieved by specifying the superclass in parentheses after the subclass name in the class definition.
```
class Subclass(Superclass):
    # subclass definition
```

### How to define a class with multiple base classes?
Multiple inheritance is achieved by specifying multiple base classes in parentheses.
```
class Subclass(BaseClass1, BaseClass2):
    # subclass definition
```

### What is the default class every class inherits from?
The default class every class inherits from is object.

### How to override a method or attribute inherited from the base class?
You can override a method or attribute by redefining it in the subclass with the desired implementation.

### Which attributes or methods are available by heritage to subclasses?
All non-private attributes and methods of the superclass are available to subclasses.

### What is the purpose of inheritance?
Inheritance allows the creation of a new class that is a modified version of an existing class, promoting code reuse and structure.

### What are, when and how to use isinstance, issubclass, type, and super built-in functions?

- **isinstance(object, class)** checks if an object is an instance of a class.

- **issubclass(class, classinfo)** checks if a class is a subclass of another class.

- **type(object)** returns the type of an object.

- **super()** returns a temporary object of the superclass, allowing access to its methods.

These functions are useful for type checking, inheritance checks, and managing class hierarchies.
