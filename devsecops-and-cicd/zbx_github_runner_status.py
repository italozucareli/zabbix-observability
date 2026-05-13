#!/usr/bin/env python3
import requests, json, sys

ORG, RUNNER_ID, TOKEN = sys.argv[1], sys.argv[2], sys.argv[3]
headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

try:
    resp = requests.get(f"https://api.github.com/orgs/{ORG}/actions/runners/{RUNNER_ID}", headers=headers).json()
    print(json.dumps({"is_online": 1 if resp.get('status') == 'online' else 0, "busy": 1 if resp.get('busy') else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))