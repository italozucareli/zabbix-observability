#!/usr/bin/env python3
import requests, json, sys

F5_HOST, F5_USER, F5_PASS = sys.argv[1], sys.argv[2], sys.argv[3]
url = f"https://{F5_HOST}/mgmt/tm/cm/failover-status"

try:
    resp = requests.get(url, auth=(F5_USER, F5_PASS), verify=False).json()
    entries = resp.get('entries', {})
    if entries:
        status_key = list(entries.keys())[0]
        state = entries[status_key]['nestedStats']['entries']['status']['description']
        print(json.dumps({"is_active": 1 if state == 'ACTIVE' else 0, "ha_state": state}))
    else:
        print(json.dumps({"error": "No failover status found"}))
except Exception as e: print(json.dumps({"error": str(e)}))