#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/apis/apiextensions.k8s.io/v1/customresourcedefinitions", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    zabbix_data = [{"{#CRD_NAME}": c['metadata']['name'], "is_v1": 1 if 'v1' in [v['name'] for v in c['spec']['versions']] else 0} for c in resp.json().get('items', [])]
    print(json.dumps({"data": zabbix_data}))
except Exception as e: print(json.dumps({"error": str(e)}))