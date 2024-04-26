#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.

Requirements:
- The email must be sent in the variable `email`
- You must use the packages `requests` and `sys`
"""

from sys import argv
import requests

if __name__ == "__main__":
    URI = argv[1]
    payload = {'email': argv[2]}
    r = requests.post(URI, data=payload)
    print(r.text)
