#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

try:
    # Utiliza a API v1 de Synthetic
    url = f"{TENANT_URL}/api/v1/synthetic/monitors"
    resp = requests.get(url, headers=headers)
    monitors = resp.json().get('monitors', [])
    
    zabbix_data = []
    for m in monitors:
        if m.get('enabled'):
            zabbix_data.append({
                "{#MONITOR_NAME}": m.get('name'),
                "{#MONITOR_ID}": m.get('entityId'),
                "{#MONITOR_TYPE}": m.get('type') # BROWSER ou HTTP
            })
            
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))