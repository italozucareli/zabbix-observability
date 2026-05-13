#!/usr/bin/env python3
import requests, json, sys

F5_HOST, F5_USER, F5_PASS = sys.argv[1], sys.argv[2], sys.argv[3]
url = f"https://{F5_HOST}/mgmt/tm/ltm/virtual"

try:
    resp = requests.get(url, auth=(F5_USER, F5_PASS), verify=False).json()
    zbx_data = [{"{#VS_NAME}": vs['name'], "{#VS_PARTITION}": vs['partition'], "{#VS_IP}": vs['destination'].split('/')[-1].split(':')[0]} for vs in resp.get('items', [])]
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))