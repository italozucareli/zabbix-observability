#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp_ns = requests.get(f"{API_URL}/api/v1/namespaces", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    resp_lr = requests.get(f"{API_URL}/api/v1/limitranges", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    lrs = {l['metadata']['namespace'] for l in resp_lr.json().get('items', [])}
    zabbix_data = [{"{#NAMESPACE}": ns['metadata']['name'], "has_limitrange": 1 if ns['metadata']['name'] in lrs else 0} for ns in resp_ns.json().get('items', [])]
    print(json.dumps({"data": zabbix_data}))
except Exception as e: print(json.dumps({"error": str(e)}))