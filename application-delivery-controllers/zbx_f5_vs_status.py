#!/usr/bin/env python3
import requests, json, sys

F5_HOST, F5_USER, F5_PASS, VS_NAME, PARTITION = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
# O til (~) é usado na API do F5 para denotar partições e subdiretórios
url = f"https://{F5_HOST}/mgmt/tm/ltm/virtual/~{PARTITION}~{VS_NAME}/stats"

try:
    resp = requests.get(url, auth=(F5_USER, F5_PASS), verify=False).json()
    entries = resp.get('entries', {})
    if entries:
        status_key = list(entries.keys())[0]
        avail_state = entries[status_key]['nestedStats']['entries']['status.availabilityState']['description']
        print(json.dumps({"is_available": 1 if avail_state == 'available' else 0, "state": avail_state}))
    else:
        print(json.dumps({"error": "No stats found"}))
except Exception as e: print(json.dumps({"error": str(e)}))