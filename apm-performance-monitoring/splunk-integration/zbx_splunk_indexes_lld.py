#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/services/data/indexes?output_mode=json&count=0", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    zbx_data = [{"{#INDEX_NAME}": i['name']} for i in resp.get('entry', []) if not i['name'].startswith('_')]
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))