#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id

Requirements:
- You must use Basic Authentication with a personal access token
as password to access to your information
- The first argument will be your username
- The second argument will be your password
- You must use the package `requests` and `sys`
"""

from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    URI = 'https://api.github.com/user'
    r = requests.get(URI, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
