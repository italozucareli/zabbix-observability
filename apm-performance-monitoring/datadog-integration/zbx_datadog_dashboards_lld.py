#!/usr/bin/env python3
import requests, json, sys

DD_SITE, DD_API_KEY, DD_APP_KEY = sys.argv[1], sys.argv[2], sys.argv[3]

url = f"https://api.{DD_SITE}/api/v1/dashboard"
headers = {"DD-API-KEY": DD_API_KEY, "DD-APPLICATION-KEY": DD_APP_KEY}

try:
    resp = requests.get(url, headers=headers, verify=False).json()
    zbx_data = [{"{#DASHBOARD_TITLE}": d['title'], "{#DASHBOARD_ID}": d['id']} for d in resp.get('dashboards', [])]
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))