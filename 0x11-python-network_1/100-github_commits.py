#!/usr/bin/python3
"""
Python script that lists the 10 most recent commits
on a given GitHub repository.

Requirements:
- The first argument will be the repository name
- The second argument will be the owner name
- You must use the packages `requests` and `sys`
"""

from sys import argv
import requests


if __name__ == "__main__":
    URI = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    r = requests.get(URI)
    commits_data = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits_data[i].get("sha"),
                commits_data[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
