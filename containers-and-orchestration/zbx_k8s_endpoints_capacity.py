#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/api/v1/endpoints", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    zabbix_data = [{"{#EP_NAME}": ep['metadata']['name'], "{#NAMESPACE}": ep['metadata']['namespace'], "address_count": sum([len(sub.get('addresses', [])) for sub in ep.get('subsets', [])])} for ep in resp.json().get('items', [])]
    print(json.dumps({"data": zabbix_data}))
except Exception as e: print(json.dumps({"error": str(e)}))