#!/usr/bin/python3
"""
script that takes 2 arguments in order to solve this challenge.
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    name = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(repo, name)

    res = requests.get(url)
    for commit in res.json()[:10]:
        sha = commit.get("sha")
        full = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, full))
