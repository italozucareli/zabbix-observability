#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/services/shcluster/status?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    content = resp['entry'][0]['content']
    print(json.dumps({"status": content.get('status'), "is_captain": 1 if content.get('captain', {}).get('is_captain') else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))