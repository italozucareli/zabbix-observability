#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, SID = sys.argv[1], sys.argv[2], sys.argv[3] # SID gerado no dispatch
try:
    resp = requests.get(f"{URL}/services/search/jobs/{SID}?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    state = resp['entry'][0]['content']['dispatchState']
    print(json.dumps({"is_done": 1 if state == 'DONE' else 0, "state": state}))
except Exception as e: print(json.dumps({"error": str(e)}))