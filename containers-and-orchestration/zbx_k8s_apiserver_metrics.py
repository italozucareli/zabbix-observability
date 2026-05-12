#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/metrics", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False, timeout=10)
    lines = resp.text.split('\n')
    errors_5xx = sum([float(l.split()[1]) for l in lines if 'apiserver_request_total' in l and 'code="5' in l])
    print(json.dumps({"total_5xx_errors": errors_5xx}))
except Exception as e: print(json.dumps({"error": str(e)}))