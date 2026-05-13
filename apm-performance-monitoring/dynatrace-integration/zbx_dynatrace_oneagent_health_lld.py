#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

try:
    url = f"{TENANT_URL}/api/v2/entities?entitySelector=type(HOST)&fields=properties.monitoringMode,properties.state"
    resp = requests.get(url, headers=headers)
    hosts = resp.json().get('entities', [])
    
    zabbix_data = []
    for h in hosts:
        props = h.get('properties', {})
        zabbix_data.append({
            "{#HOST_NAME}": h.get('displayName'),
            "{#ENTITY_ID}": h.get('entityId'),
            "monitoring_mode": props.get('monitoringMode', 'UNKNOWN'),
            "agent_state": props.get('state', 'UNKNOWN')
        })
        
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))