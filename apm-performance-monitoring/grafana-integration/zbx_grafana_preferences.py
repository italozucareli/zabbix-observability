#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/api/org/preferences", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"home_dashboard_id": resp.get('homeDashboardId', 0), "theme": resp.get('theme', 'default')}))
except Exception as e: print(json.dumps({"error": str(e)}))