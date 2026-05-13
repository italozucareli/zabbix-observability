#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

try:
    url = f"{TENANT_URL}/api/v2/entities?entitySelector=type(PROCESS_GROUP)"
    resp = requests.get(url, headers=headers)
    groups = resp.json().get('entities', [])
    
    zabbix_data = []
    for g in groups:
        zabbix_data.append({
            "{#PROCESS_GROUP_NAME}": g.get('displayName'),
            "{#PROCESS_GROUP_ID}": g.get('entityId')
        })
        
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))