#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2] # Requer admin
try:
    resp = requests.get(f"{URL}/api/admin/ldap-sync-status", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"ldap_sync_success": 1 if resp.get('status') == 'success' else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))