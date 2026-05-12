#!/usr/bin/env python3
import requests, json, sys
requests.packages.urllib3.disable_warnings()

API_URL = sys.argv[1]
TOKEN = sys.argv[2]
headers = {"Authorization": f"Bearer {TOKEN}"}

try:
    resp = requests.get(f"{API_URL}/api/v1/pods", headers=headers, verify=False, timeout=15)
    resp.raise_for_status()
    pods = resp.json().get('items', [])
    
    oom_count = 0
    oom_pods = []
    
    for pod in pods:
        statuses = pod.get('status', {}).get('containerStatuses', [])
        for cs in statuses:
            term_reason = cs.get('state', {}).get('terminated', {}).get('reason', '')
            if term_reason == 'OOMKilled':
                oom_count += 1
                oom_pods.append(f"{pod['metadata']['namespace']}/{pod['metadata']['name']}")
                
    # Retorna o total absoluto e a lista para logs no Zabbix
    print(json.dumps({
        "total_oomkilled": oom_count,
        "affected_pods": ", ".join(oom_pods) if oom_pods else "None"
    }))
except Exception as e:
    print(json.dumps({"error": str(e)}))