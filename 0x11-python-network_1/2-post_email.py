#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

Requirements:
- The email must be sent in the email variable
- You must use the packages urllib and sys
"""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    URI = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(URI, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
