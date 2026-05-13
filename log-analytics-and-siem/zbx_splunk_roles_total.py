#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/services/authorization/roles?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"total_roles": len(resp.get('entry', []))}))
except Exception as e: print(json.dumps({"error": str(e)}))