#!/usr/bin/python3
"""
script that takes 2 arguments in order to solve this challenge.
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[2]
    name = sys.argv[1]

    url = "https://api.github.com/repos/{}/{}/commits".format(repo, name)

    res = requests.get(url, params={"per_page": 10})
    for commit in res.json():
        sha = commit.get("sha")
        full = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, full))
