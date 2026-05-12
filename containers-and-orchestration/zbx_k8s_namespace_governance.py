#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
REQUIRED_LABEL = "team"
try:
    resp = requests.get(f"{API_URL}/api/v1/namespaces", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    zabbix_data = [{"{#NAMESPACE}": ns['metadata']['name'], "compliant": 1 if REQUIRED_LABEL in ns['metadata'].get('labels', {}) else 0} for ns in resp.json().get('items', [])]
    print(json.dumps({"data": zabbix_data}))
except Exception as e: print(json.dumps({"error": str(e)}))