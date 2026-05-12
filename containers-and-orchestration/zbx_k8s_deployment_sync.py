#!/usr/bin/env python3
import requests, json, sys
requests.packages.urllib3.disable_warnings()

API_URL = sys.argv[1]
TOKEN = sys.argv[2]
headers = {"Authorization": f"Bearer {TOKEN}"}

try:
    resp = requests.get(f"{API_URL}/apis/apps/v1/deployments", headers=headers, verify=False, timeout=10)
    resp.raise_for_status()
    deps = resp.json().get('items', [])
    
    zabbix_data = []
    for d in deps:
        generation = d['metadata'].get('generation', 1)
        observed = d.get('status', {}).get('observedGeneration', 0)
        
        zabbix_data.append({
            "{#DEPLOYMENT_NAME}": d['metadata']['name'],
            "{#NAMESPACE}": d['metadata']['namespace'],
            "in_sync": 1 if generation == observed else 0,
            "unavailable_replicas": d.get('status', {}).get('unavailableReplicas', 0)
        })
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))