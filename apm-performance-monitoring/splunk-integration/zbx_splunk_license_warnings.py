#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/services/licenser/messages?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    warnings = [m for m in resp.get('entry', []) if m['content'].get('category') == 'license_warning']
    print(json.dumps({"license_warnings_count": len(warnings)}))
except Exception as e: print(json.dumps({"error": str(e)}))