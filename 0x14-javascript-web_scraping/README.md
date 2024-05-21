# Web Scrapping with JavaScript
JavaScript is a powerful and versatile programming language with several attributes that make it amazing:

- **Ubiquity:** JavaScript is the language of the web, running in every browser. It's essential for creating dynamic and interactive web pages.
- **Versatility:** It can be used for both client-side and server-side development (thanks to Node.js), making it a full-stack language.
- **Large Ecosystem:** JavaScript has a rich ecosystem of libraries and frameworks (e.g., React, Angular, Vue.js) that simplify development.
- **Event-Driven Programming:** JavaScript's asynchronous capabilities (promises, async/await) are ideal for handling I/O-heavy operations.
- **Community and Resources:** A vast community and extensive resources make learning and troubleshooting easier.
- **Prototyping Speed:** Its dynamic nature allows for rapid prototyping and iteration.

### How to Manipulate JSON Data
JSON (JavaScript Object Notation) is a lightweight data interchange format. Here are common operations for manipulating JSON data in JavaScript:

- **Parsing JSON:** Convert a JSON string into a JavaScript object.
```
const jsonString = '{"name": "John", "age": 30}';
const jsonObject = JSON.parse(jsonString);
console.log(jsonObject.name); // Output: John
```

- **Stringifying JSON:** Convert a JavaScript object into a JSON string.
```
const jsonObject = { name: "John", age: 30 };
const jsonString = JSON.stringify(jsonObject);
console.log(jsonString); // Output: {"name":"John","age":30}
```

- **Accessing Data:**
```
const jsonObject = JSON.parse('{"name": "John", "age": 30}');
console.log(jsonObject.name); // Output: John
console.log(jsonObject.age); // Output: 30
```

- **Modifying Data:**
```
jsonObject.name = "Jane";
jsonObject.age = 25;
console.log(JSON.stringify(jsonObject)); // Output: {"name":"Jane","age":25}
```

### How to Use request and fetch API
- **Using the fetch API:** A modern way to make network requests.
```
// GET request
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));

// POST request
fetch('https://api.example.com/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ name: 'John', age: 30 })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

- **Using the request Module in Node.js:** The request module is deprecated; it's recommended to use the axios or node-fetch modules instead.

- **Using axios:**
```
// GET request
axios.get('https://api.example.com/data')
  .then(response => console.log(response.data))
  .catch(error => console.error('Error:', error));

// POST request
axios.post('https://api.example.com/data', {
  name: 'John',
  age: 30
})
  .then(response => console.log(response.data))
  .catch(error => console.error('Error:', error));
```

- **Using node-fetch:**
```
const fetch = require('node-fetch');

// GET request
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));

// POST request
fetch('https://api.example.com/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ name: 'John', age: 30 })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### How to Read and Write a File Using fs Module
The fs (File System) module in Node.js allows you to interact with the file system.

- **Reading a File:**
```
const fs = require('fs');

// Asynchronous read
fs.readFile('path/to/file.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

// Synchronous read
try {
  const data = fs.readFileSync('path/to/file.txt', 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
```

- **Writing to a File:**
```
const fs = require('fs');

// Asynchronous write
const content = 'Some content to write';
fs.writeFile('path/to/file.txt', content, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File has been written');
});

// Synchronous write
try {
  fs.writeFileSync('path/to/file.txt', content, 'utf8');
  console.log('File has been written');
} catch (err) {
  console.error(err);
}
```