#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, USERNAME = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/services/authentication/users/{USERNAME}?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    locked = resp['entry'][0]['content']['locked-out']
    print(json.dumps({"is_locked_out": 1 if locked else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))