#!/usr/bin/env python3
import requests, json, sys

ORG, TOKEN = sys.argv[1], sys.argv[2]
headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

try:
    resp = requests.get(f"https://api.github.com/orgs/{ORG}/actions/runners", headers=headers).json()
    zbx_data = [{"{#RUNNER_NAME}": r['name'], "{#RUNNER_ID}": r['id'], "{#RUNNER_OS}": r['os']} for r in resp.get('runners', [])]
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))