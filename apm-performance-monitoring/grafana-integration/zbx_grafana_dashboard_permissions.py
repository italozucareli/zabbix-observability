#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, DASH_ID = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/api/dashboards/id/{DASH_ID}/permissions", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    public_edit = len([p for p in resp if p.get('role') == 'Viewer' and p.get('permission') == 2])
    print(json.dumps({"security_risk_viewer_edit": 1 if public_edit > 0 else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))