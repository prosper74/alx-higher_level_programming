# Python - Network

### What a URL is?
A URL (Uniform Resource Locator) is a reference or address to a resource on the internet. It typically consists of several components, including the scheme (such as HTTP or HTTPS), the domain name, optional port number, path, query parameters, and fragment identifier.

### What HTTP is?
HTTP (Hypertext Transfer Protocol) is the underlying protocol used for transmitting data on the World Wide Web. It defines how messages are formatted and transmitted, as well as how web servers and browsers should respond to various commands.

### How to read a URL
Reading a URL involves understanding its components:

- Scheme: Indicates the protocol being used (e.g., HTTP, HTTPS, FTP).
- Domain name: Identifies the specific web server hosting the resource.
- Sub-domain: Optionally, a domain can be divided into smaller sections, each of which can be a sub-domain.
- Port number: Specifies the port on the server to which the request should be sent. Default HTTP port is 80, and HTTPS is 443.
- Path: Specifies the location of the resource on the server.
- Query string: Contains additional parameters or data to be sent to the server.
- Fragment identifier: Specifies a specific section within the resource.

### The scheme for a HTTP URL
The scheme for an HTTP URL is typically "http://" or "https://", indicating whether the connection should be secure or not.

### What a domain name is
A domain name is a human-readable label that represents an IP address of a specific server or group of servers on the internet. It's used to easily identify and access websites.

### What a sub-domain is
A sub-domain is a subdivision of a domain, used to organize and navigate within larger domain spaces. For example, "blog.example.com" is a sub-domain of "example.com".

### How to define a port number in a URL
To define a port number in a URL, you append ":port_number" after the domain name. For example, "http://example.com:8080".

### What a query string is
A query string is a part of a URL that contains additional parameters or data to be sent to the server. It typically follows the path and is preceded by a question mark (?).

### What an HTTP request is
An HTTP request is a message sent from a client (such as a web browser) to a server, requesting a specific action or resource. It consists of a request line, headers, and optionally, a message body.

### What an HTTP response is
An HTTP response is a message sent from a server back to the client in response to an HTTP request. It contains a response line, headers, and optionally, a message body.

### What HTTP headers are
HTTP headers are additional information sent with HTTP requests and responses, providing metadata about the message or the resource being requested or provided.

### What the HTTP message body is
The HTTP message body contains the data being transmitted in an HTTP request or response. It's optional and can contain any type of data, such as HTML, JSON, or binary data.

### What an HTTP request method is
HTTP defines several request methods (also known as verbs) that indicate the desired action to be performed on a resource, such as GET, POST, PUT, DELETE, etc.

### What an HTTP response status code is
An HTTP response status code indicates the success or failure of an HTTP request. Status codes are three-digit numbers, with the first digit indicating the general type of response (e.g., 2xx for success, 4xx for client errors, 5xx for server errors).

### What an HTTP Cookie is
An HTTP Cookie is a small piece of data sent from a website and stored on the user's device by the web browser. Cookies are commonly used for tracking user sessions, authentication, and personalization.

### How to make a request with cURL
To make a request with cURL (Command Line URL), you use the curl command followed by the URL you want to access. You can include additional options to customize the request, such as headers, request methods, data, etc.

### What happens when you type google.com in your browser (Application level)
When you type "google.com" in your browser at the application level, the browser initiates a DNS (Domain Name System) lookup to find the IP address associated with the domain name "google.com". Once the IP address is obtained, the browser sends an HTTP request to the server at that IP address, typically requesting the default page or the page specified in the URL. The server then responds with the requested web page, and the browser renders it for the user to view and interact with.