#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/api/auth/keys", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    zbx_data = [{"{#APIKEY_NAME}": k['name'], "{#APIKEY_ID}": k['id']} for k in resp]
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))