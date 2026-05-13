#!/usr/bin/env python3
import requests, json, sys

DD_SITE, DD_API_KEY, DD_APP_KEY, PUBLIC_ID = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

url = f"https://api.{DD_SITE}/api/v1/synthetics/tests/{PUBLIC_ID}"
headers = {"DD-API-KEY": DD_API_KEY, "DD-APPLICATION-KEY": DD_APP_KEY}

try:
    resp = requests.get(url, headers=headers, verify=False).json()
    status = resp.get('status', 'unknown')
    print(json.dumps({"is_live": 1 if status == 'live' else 0, "status": status}))
except Exception as e: print(json.dumps({"error": str(e)}))