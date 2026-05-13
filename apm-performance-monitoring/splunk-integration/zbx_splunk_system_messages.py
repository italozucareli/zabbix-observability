#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/services/messages?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    msgs = [m for m in resp.get('entry', []) if m['content']['severity'] in ['error', 'warn']]
    print(json.dumps({"active_system_alerts": len(msgs)}))
except Exception as e: print(json.dumps({"error": str(e)}))