#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2] # Requer Admin
try:
    resp = requests.get(f"{URL}/api/admin/settings", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    allow = resp.get('users', {}).get('allow_sign_up', 'false')
    print(json.dumps({"allow_sign_up_enabled": 1 if allow == 'true' else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))