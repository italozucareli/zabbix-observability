#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, DASH_UID = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/api/dashboards/uid/{DASH_UID}", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps(resp.get('dashboard', {})))
except Exception as e: print(json.dumps({"error": str(e)}))