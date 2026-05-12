#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/apis/batch/v1/jobs", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    zabbix_data = [{"{#JOB}": j['metadata']['name'], "{#NAMESPACE}": j['metadata']['namespace'], "failed": j.get('status', {}).get('failed', 0), "succeeded": j.get('status', {}).get('succeeded', 0)} for j in resp.json().get('items', [])]
    print(json.dumps({"data": zabbix_data}))
except Exception as e: print(json.dumps({"error": str(e)}))