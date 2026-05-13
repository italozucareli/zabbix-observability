#!/usr/bin/env python3
import requests, json, sys

OWNER, REPO, TOKEN = sys.argv[1], sys.argv[2], sys.argv[3]
headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

try:
    resp = requests.get(f"https://api.github.com/repos/{OWNER}/{REPO}", headers=headers).json()
    print(json.dumps({"size_kb": resp.get('size', 0)}))
except Exception as e: print(json.dumps({"error": str(e)}))