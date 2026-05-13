#!/usr/bin/env python3
import requests, json, sys

DD_SITE, DD_API_KEY, DD_APP_KEY, INDEX_NAME = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

url = f"https://api.{DD_SITE}/api/v1/logs/config/indexes/{INDEX_NAME}"
headers = {"DD-API-KEY": DD_API_KEY, "DD-APPLICATION-KEY": DD_APP_KEY}

try:
    resp = requests.get(url, headers=headers, verify=False).json()
    print(json.dumps({"retention_days": resp.get('num_retention_days', 0)}))
except Exception as e: print(json.dumps({"error": str(e)}))