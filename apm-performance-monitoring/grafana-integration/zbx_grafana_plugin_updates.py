#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, PLUGIN_ID = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/api/plugins/{PLUGIN_ID}", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"update_available": 1 if resp.get('hasUpdate') else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))