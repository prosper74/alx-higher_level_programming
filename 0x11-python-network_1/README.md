# Python - Network #1

### How to fetch internet resources with the Python package urllib
The `urllib` module in Python provides an interface for fetching URLs (Uniform Resource Locators). Here's a basic example of how to fetch a URL using `urllib.request`:
```
import urllib.request

# Fetch a URL
with urllib.request.urlopen('https://example.com') as response:
    html = response.read()
    print(html)
```

### How to decode urllib body response
The `response.read()` method returns `bytes`. If you want to decode the bytes into a string, you can specify the encoding:
```
import urllib.request

with urllib.request.urlopen('https://example.com') as response:
    html = response.read().decode('utf-8')
    print(html)
```


### How to use the Python package `requests` (#requestsiswaysimplerthanurllib)
The requests library is a popular third-party Python library that provides a more user-friendly interface for making HTTP requests. It simplifies many aspects of fetching URLs and handling responses.
```
import requests

# Fetch a URL
response = requests.get('https://example.com')
html = response.text
print(html)
```

### How to make HTTP GET request
Both `urllib` and `requests` can be used to make HTTP `GET requests`. With `requests`, you can use the `requests.get()` method:
```
import requests

response = requests.get('https://example.com/api/data')
json_data = response.json()
print(json_data)
```

### How to make HTTP POST/PUT/etc. request
For other `HTTP` methods like `POST`, `PUT`, `DELETE`, etc., you can use the corresponding methods in requests:
```
import requests

data = {'key': 'value'}
response = requests.post('https://example.com/api/data', json=data)
print(response.status_code)
```

### How to fetch JSON resources
When fetching `JSON` resources, you can use the `response.json()` method with `requests` to automatically parse the JSON data:
```
import requests

response = requests.get('https://example.com/api/data')
json_data = response.json()
print(json_data)
```

### How to manipulate data from an external service
Once you have fetched data from an external service (e.g., a JSON API), you can manipulate and process the data using Python's built-in data structures and libraries like `json`, `pandas`, etc.
```
import requests

response = requests.get('https://example.com/api/data')
json_data = response.json()

# Manipulate the data
filtered_data = [item for item in json_data if item['value'] > 10]
print(filtered_data)
```