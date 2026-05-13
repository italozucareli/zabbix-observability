#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, PEER = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/services/search/distributed/peers/{PEER}?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    status = resp['entry'][0]['content']['status']
    print(json.dumps({"is_up": 1 if status == 'Up' else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))