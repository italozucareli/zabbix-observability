#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, REPORT_ID = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/api/reports/{REPORT_ID}", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"last_state": resp.get('state', 'Unknown')}))
except Exception as e: print(json.dumps({"error": str(e)}))