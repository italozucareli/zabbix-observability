#!/usr/bin/env python3
import requests, json, sys
requests.packages.urllib3.disable_warnings()

API_URL = sys.argv[1]
TOKEN = sys.argv[2]
headers = {"Authorization": f"Bearer {TOKEN}"}

try:
    resp = requests.get(f"{API_URL}/apis/batch/v1/cronjobs", headers=headers, verify=False, timeout=10)
    resp.raise_for_status()
    cronjobs = resp.json().get('items', [])
    
    zabbix_data = []
    for cj in cronjobs:
        suspend = cj['spec'].get('suspend', False)
        active_jobs = len(cj.get('status', {}).get('active', []))
        last_schedule = cj.get('status', {}).get('lastScheduleTime', 'Never')
        
        zabbix_data.append({
            "{#CRONJOB_NAME}": cj['metadata']['name'],
            "{#NAMESPACE}": cj['metadata']['namespace'],
            "is_suspended": 1 if suspend else 0,
            "active_executions": active_jobs,
            "has_scheduled_before": 1 if last_schedule != 'Never' else 0
        })
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))