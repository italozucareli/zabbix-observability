#!/usr/bin/env python3
import requests, json, sys

F5_HOST, F5_USER, F5_PASS = sys.argv[1], sys.argv[2], sys.argv[3]
url = f"https://{F5_HOST}/mgmt/tm/ltm/pool"

try:
    resp = requests.get(url, auth=(F5_USER, F5_PASS), verify=False).json()
    zbx_data = [{"{#POOL_NAME}": p['name'], "{#POOL_PARTITION}": p['partition']} for p in resp.get('items', [])]
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))