#!/bin/bash
# sends a JSON
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
