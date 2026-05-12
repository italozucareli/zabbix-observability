#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/apis/apps/v1/statefulsets", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    zabbix_data = [{"{#STS_NAME}": s['metadata']['name'], "synced": 1 if s.get('status', {}).get('currentRevision') == s.get('status', {}).get('updateRevision') else 0} for s in resp.json().get('items', [])]
    print(json.dumps({"data": zabbix_data}))
except Exception as e: print(json.dumps({"error": str(e)}))