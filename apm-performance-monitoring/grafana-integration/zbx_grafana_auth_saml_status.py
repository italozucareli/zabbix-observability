#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/api/admin/settings", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    saml_enabled = resp.get('auth.saml', {}).get('enabled', 'false')
    print(json.dumps({"saml_enabled": 1 if saml_enabled == 'true' else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))