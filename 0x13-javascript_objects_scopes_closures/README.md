# JavaScript - Objects, Scopes and Closures
JavaScript is a high-level, interpreted programming language primarily known for its role in web development. It's characterized by its dynamic, flexible nature and is widely used for both client-side and server-side scripting. Developed by Netscape in 1995 initially to make web pages more interactive, JavaScript has since evolved into a versatile language powering a vast array of applications, including web and mobile apps, desktop software, and even server-side development.

### JavaScript programming is amazing for several reasons:

- Versatility: JavaScript can be used for both client-side and server-side development, allowing developers to build full-stack applications entirely in one language.
- Ubiquity: JavaScript is supported by all major web browsers, making it accessible to a wide audience and enabling developers to create interactive web experiences.
- Dynamic Typing: JavaScript's dynamic typing allows for flexible and expressive coding, making it easier to write and maintain code.
- Asynchronous Programming: JavaScript supports asynchronous programming paradigms, allowing developers to handle events, network requests, and other tasks without blocking the main execution thread.
- Rich Ecosystem: JavaScript has a vast ecosystem of libraries, frameworks, and tools that streamline development tasks and empower developers to build complex applications efficiently.

### Object Litterals
To create an object in JavaScript, you can use either object literal syntax or the Object constructor:

- Object literal syntax:
```
let person = {
    name: 'John',
    age: 30,
    email: 'john@example.com'
};
```

- Object Constructor:
```
let person = new Object();
person.name = 'John';
person.age = 30;
person.email = 'john@example.com';
```

### `this` in Javascript
In JavaScript, this refers to the context in which a function is executed. It typically refers to the object that owns the function being executed.

### What undefined means
`undefined` in JavaScript represents a variable that has been declared but not assigned a value.

### Why the variable type and scope is important
Variable type and scope are important in JavaScript for ensuring code reliability, readability, and maintainability. Understanding variable types helps developers write code that behaves as expected, while proper scoping ensures that variables are accessible only where needed, preventing unintended side effects and bugs.

### What is a closure
A `closure` in JavaScript is a function that has access to its own scope, as well as the scope in which it was created. Closures are often used to encapsulate data and create private variables in JavaScript.

### What is a prototype
A prototype in JavaScript is a mechanism for object inheritance. Every JavaScript object has a prototype property, which allows objects to inherit properties and methods from other objects.

### How to inherit an object from another
To inherit an object from another in JavaScript, you can use prototype-based inheritance. Here's an example:
```
function Animal(name) {
    this.name = name;
}

Animal.prototype.walk = function() {
    console.log(this.name + ' is walking.');
}

function Dog(name) {
    Animal.call(this, name);
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

let dog = new Dog('Buddy');
dog.walk(); // Output: Buddy is walking.
```

In this example, the Dog constructor function inherits from the Animal constructor function by setting Dog.prototype to a new object created with Object.create(Animal.prototype). This allows instances of Dog to access the walk method defined in the Animal prototype.