#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/apis/apiregistration.k8s.io/v1/apiservices", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    zabbix_data = [{"{#APISERVICE}": a['metadata']['name'], "available": 1 if any(c['type'] == 'Available' and c['status'] == 'True' for c in a.get('status', {}).get('conditions', [])) else 0} for a in resp.json().get('items', [])]
    print(json.dumps({"data": zabbix_data}))
except Exception as e: print(json.dumps({"error": str(e)}))