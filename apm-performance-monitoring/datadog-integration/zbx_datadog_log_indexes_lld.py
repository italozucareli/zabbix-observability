#!/usr/bin/env python3
import requests, json, sys

DD_SITE, DD_API_KEY, DD_APP_KEY = sys.argv[1], sys.argv[2], sys.argv[3]

url = f"https://api.{DD_SITE}/api/v1/logs/config/indexes"
headers = {"DD-API-KEY": DD_API_KEY, "DD-APPLICATION-KEY": DD_APP_KEY}

try:
    resp = requests.get(url, headers=headers, verify=False).json()
    zbx_data = [{"{#INDEX_NAME}": i['name'], "{#RETENTION_DAYS}": i['num_retention_days']} for i in resp.get('indexes', [])]
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))