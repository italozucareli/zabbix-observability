#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/api/v1/pods?fieldSelector=status.phase=Failed", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    evicted = [p for p in resp.json().get('items', []) if p.get('status', {}).get('reason') == 'Evicted']
    print(json.dumps({"total_evicted": len(evicted)}))
except Exception as e: print(json.dumps({"error": str(e)}))