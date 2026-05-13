#!/usr/bin/env python3
import requests, json, sys

ORG, TOKEN = sys.argv[1], sys.argv[2]
headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

try:
    resp = requests.get(f"https://api.github.com/orgs/{ORG}/settings/billing/actions", headers=headers).json()
    print(json.dumps({"total_minutes_used": resp.get('total_minutes_used', 0)}))
except Exception as e: print(json.dumps({"error": str(e)}))