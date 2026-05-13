#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/api/users", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    admins = len([u for u in resp if u.get('isAdmin')])
    print(json.dumps({"total_server_admins": admins}))
except Exception as e: print(json.dumps({"error": str(e)}))