#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/services/kvstore/status?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    status = resp['entry'][0]['content']['current']['status']
    print(json.dumps({"kvstore_ready": 1 if status == 'ready' else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))