#!/usr/bin/python3
"""
Python script that lists the 10 most recent commits
on a given GitHub repository.

Requirements:
- The first argument will be the repository name
- The second argument will be the owner name
- You must use the packages `requests` and `sys`
"""

import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
