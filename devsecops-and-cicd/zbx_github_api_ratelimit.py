#!/usr/bin/env python3
import requests, json, sys

TOKEN = sys.argv[1]
headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

try:
    resp = requests.get("https://api.github.com/rate_limit", headers=headers).json()
    core = resp.get('resources', {}).get('core', {})
    print(json.dumps({"limit": core.get('limit'), "remaining": core.get('remaining')}))
except Exception as e: print(json.dumps({"error": str(e)}))