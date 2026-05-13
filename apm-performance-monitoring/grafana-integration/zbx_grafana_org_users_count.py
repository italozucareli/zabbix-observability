#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, ORG_ID = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/api/orgs/{ORG_ID}/users", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"org_users_total": len(resp)}))
except Exception as e: print(json.dumps({"error": str(e)}))