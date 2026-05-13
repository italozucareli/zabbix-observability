#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, SA_ID = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/api/serviceaccounts/{SA_ID}/tokens", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"active_tokens": len([t for t in resp if not t.get('hasExpired')])}))
except Exception as e: print(json.dumps({"error": str(e)}))