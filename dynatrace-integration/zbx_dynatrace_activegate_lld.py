#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

try:
    # A API de ActiveGates fica na v2
    url = f"{TENANT_URL}/api/v2/activeGates"
    resp = requests.get(url, headers=headers)
    active_gates = resp.json().get('activeGates', [])
    
    zabbix_data = []
    for ag in active_gates:
        zabbix_data.append({
            "{#AG_NAME}": ag.get('networkAddress', 'Unknown'),
            "{#AG_ID}": ag.get('id'),
            "{#AG_OS}": ag.get('osType'),
            "is_online": 1 if ag.get('networkStatus') == 'ONLINE' else 0
        })
        
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))