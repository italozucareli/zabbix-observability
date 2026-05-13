#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, UID = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/api/datasources/uid/{UID}/health", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"is_healthy": 1 if resp.get('status') == 'success' else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))