#!/usr/bin/env python3
import requests, json, sys
requests.packages.urllib3.disable_warnings()

API_URL = sys.argv[1] # ex: https://10.0.0.1:6443
TOKEN = sys.argv[2]

headers = {"Authorization": f"Bearer {TOKEN}"}

try:
    resp = requests.get(f"{API_URL}/api/v1/nodes", headers=headers, verify=False, timeout=10)
    resp.raise_for_status()
    nodes = resp.json().get('items', [])
    
    zabbix_data = []
    for node in nodes:
        name = node['metadata']['name']
        conditions = {c['type']: 1 if c['status'] == 'True' else 0 for c in node['status']['conditions']}
        
        zabbix_data.append({
            "{#NODE_NAME}": name,
            "ready": conditions.get('Ready', 0),
            "memory_pressure": conditions.get('MemoryPressure', 0),
            "disk_pressure": conditions.get('DiskPressure', 0),
            "pid_pressure": conditions.get('PIDPressure', 0)
        })
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))