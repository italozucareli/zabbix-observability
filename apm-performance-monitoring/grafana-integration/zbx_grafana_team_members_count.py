#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, TEAM_ID = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/api/teams/{TEAM_ID}/members", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"team_members_total": len(resp)}))
except Exception as e: print(json.dumps({"error": str(e)}))