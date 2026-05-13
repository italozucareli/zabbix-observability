#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/services/licenser/pools?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    pool = resp['entry'][0]['content']
    used, quota = int(pool['used_bytes']), int(pool['effective_quota'])
    print(json.dumps({"license_used_percent": round((used / quota) * 100, 2) if quota > 0 else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))