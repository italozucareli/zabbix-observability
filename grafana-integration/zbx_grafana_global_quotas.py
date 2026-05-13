#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/api/admin/quotas", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    quotas = {q['target']: q['limit'] for q in resp}
    print(json.dumps(quotas))
except Exception as e: print(json.dumps({"error": str(e)}))