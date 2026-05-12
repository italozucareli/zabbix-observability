#!/usr/bin/env python3
import requests, json, sys
requests.packages.urllib3.disable_warnings()

API_URL = sys.argv[1]
TOKEN = sys.argv[2]
headers = {"Authorization": f"Bearer {TOKEN}"}

try:
    resp = requests.get(f"{API_URL}/apis/autoscaling/v2/horizontalpodautoscalers", headers=headers, verify=False, timeout=10)
    resp.raise_for_status()
    hpas = resp.json().get('items', [])
    
    zabbix_data = []
    for hpa in hpas:
        zabbix_data.append({
            "{#HPA_NAME}": hpa['metadata']['name'],
            "{#NAMESPACE}": hpa['metadata']['namespace'],
            "min_replicas": hpa['spec'].get('minReplicas', 1),
            "max_replicas": hpa['spec']['maxReplicas'],
            "current_replicas": hpa.get('status', {}).get('currentReplicas', 0),
            "desired_replicas": hpa.get('status', {}).get('desiredReplicas', 0)
        })
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))