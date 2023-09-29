#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    try:
        res = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
        data = res.json()

        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data["id"], data["name"]))

    except Exception:
        print("Not a valid JSON")
