#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/services/deployment/server/clients?output_mode=json&count=0", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    zbx_data = [{"{#CLIENT_NAME}": c['content']['hostname'], "{#CLIENT_IP}": c['content']['ip']} for c in resp.get('entry', [])]
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))