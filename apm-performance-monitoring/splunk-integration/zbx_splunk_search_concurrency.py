#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/services/server/status/resource-usage/hostwide?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    searches = resp['entry'][0]['content'].get('active_hist_searches', 0)
    print(json.dumps({"active_searches": int(searches)}))
except Exception as e: print(json.dumps({"error": str(e)}))