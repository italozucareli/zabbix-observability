#!/usr/bin/env python3
import requests, json, sys

F5_HOST, F5_USER, F5_PASS = sys.argv[1], sys.argv[2], sys.argv[3]
url = f"https://{F5_HOST}/mgmt/tm/cm/sync-status"

try:
    resp = requests.get(url, auth=(F5_USER, F5_PASS), verify=False).json()
    entries = resp.get('entries', {})
    if entries:
        status_key = list(entries.keys())[0]
        sync_state = entries[status_key]['nestedStats']['entries']['status']['description']
        print(json.dumps({"in_sync": 1 if sync_state == 'In Sync' else 0, "status": sync_state}))
    else:
        print(json.dumps({"error": "No sync status found"}))
except Exception as e: print(json.dumps({"error": str(e)}))