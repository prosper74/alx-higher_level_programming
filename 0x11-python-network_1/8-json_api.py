#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.

Requirement:
- You must use the package `requests` and `sys`
"""

from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        arg_letter = ""
    else:
        arg_letter = argv[1]
    URI = 'http://0.0.0.0:5000/search_user'
    payload = {'q': arg_letter}
    r = requests.post(URI, data=payload)

    try:
        dic = r.json()
        if dic:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
