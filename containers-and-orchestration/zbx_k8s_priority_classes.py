#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/apis/scheduling.k8s.io/v1/priorityclasses", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    zabbix_data = [{"{#PRIORITY_CLASS}": p['metadata']['name'], "value": p['value']} for p in resp.json().get('items', [])]
    print(json.dumps({"data": zabbix_data}))
except Exception as e: print(json.dumps({"error": str(e)}))