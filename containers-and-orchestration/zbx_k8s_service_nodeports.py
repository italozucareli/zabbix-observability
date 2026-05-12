#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/api/v1/services", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    zabbix_data = [{"{#SVC_NAME}": s['metadata']['name'], "node_port": port.get('nodePort', 0)} for s in resp.json().get('items', []) for port in s.get('spec', {}).get('ports', []) if port.get('nodePort')]
    print(json.dumps({"data": zabbix_data}))
except Exception as e: print(json.dumps({"error": str(e)}))