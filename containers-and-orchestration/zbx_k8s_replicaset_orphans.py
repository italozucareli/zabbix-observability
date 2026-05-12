#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/apis/apps/v1/replicasets", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    zabbix_data = [{"{#RS_NAME}": r['metadata']['name'], "replicas": r['status'].get('replicas', 0)} for r in resp.json().get('items', []) if r['status'].get('replicas', 0) == 0]
    print(json.dumps({"orphans_count": len(zabbix_data), "data": zabbix_data}))
except Exception as e: print(json.dumps({"error": str(e)}))