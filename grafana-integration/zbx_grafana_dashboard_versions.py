#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, UID = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/api/dashboards/uid/{UID}/versions", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"total_versions": len(resp)}))
except Exception as e: print(json.dumps({"error": str(e)}))