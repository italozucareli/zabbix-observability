#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, DS_ID = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/api/datasources/{DS_ID}/permissions", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"custom_permissions_count": len(resp)}))
except Exception as e: print(json.dumps({"error": str(e)}))