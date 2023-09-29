#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]

    try:
        res = requests.get("https://api.github.com/user", auth=(user, passw))
        if res.status_code == 200:
            print(res.json().get("id"))
        else:
            print("None")
    except Exception:
        print("None")
