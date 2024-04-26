#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status

Requirement:
- You must use the package `requests`
"""

import requests

if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
