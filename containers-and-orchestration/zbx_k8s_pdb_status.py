#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
headers = {"Authorization": f"Bearer {TOKEN}"}
try:
    resp = requests.get(f"{API_URL}/apis/policy/v1/poddisruptionbudgets", headers=headers, verify=False, timeout=10)
    zabbix_data = [{"{#PDB_NAME}": p['metadata']['name'], "{#NAMESPACE}": p['metadata']['namespace'], "allowed_disruptions": p.get('status', {}).get('disruptionsAllowed', 0), "current_healthy": p.get('status', {}).get('currentHealthy', 0)} for p in resp.json().get('items', [])]
    print(json.dumps({"data": zabbix_data}))
except Exception as e: print(json.dumps({"error": str(e)}))