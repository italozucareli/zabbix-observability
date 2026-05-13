#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/services/licenser/licenses?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    total_bytes = sum([int(l['content']['quota']) for l in resp.get('entry', [])])
    print(json.dumps({"total_capacity_gb": total_bytes / (1024**3)}))
except Exception as e: print(json.dumps({"error": str(e)}))