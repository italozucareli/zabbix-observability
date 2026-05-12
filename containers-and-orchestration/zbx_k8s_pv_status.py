#!/usr/bin/env python3
import requests, json, sys
requests.packages.urllib3.disable_warnings()

API_URL = sys.argv[1]
TOKEN = sys.argv[2]
headers = {"Authorization": f"Bearer {TOKEN}"}

try:
    resp = requests.get(f"{API_URL}/api/v1/persistentvolumes", headers=headers, verify=False, timeout=10)
    resp.raise_for_status()
    pvs = resp.json().get('items', [])
    
    zabbix_data = []
    for pv in pvs:
        phase = pv.get('status', {}).get('phase', 'Unknown')
        zabbix_data.append({
            "{#PV_NAME}": pv['metadata']['name'],
            "{#CAPACITY}": pv['spec']['capacity']['storage'],
            "phase": phase,
            "status_code": 1 if phase == "Bound" else (2 if phase == "Available" else 0)
        })
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))