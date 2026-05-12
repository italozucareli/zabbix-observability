#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/api/v1/resourcequotas", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    zabbix_data = [{"{#QUOTA}": q['metadata']['name'], "{#NAMESPACE}": q['metadata']['namespace'], "cpu_used": q['status']['used'].get('limits.cpu', '0'), "cpu_hard": q['status']['hard'].get('limits.cpu', '0')} for q in resp.json().get('items', [])]
    print(json.dumps({"data": zabbix_data}))
except Exception as e: print(json.dumps({"error": str(e)}))