#!/usr/bin/env python3
import requests, json, sys

F5_HOST, F5_USER, F5_PASS, POOL_NAME, PARTITION = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
url = f"https://{F5_HOST}/mgmt/tm/ltm/pool/~{PARTITION}~{POOL_NAME}/members/stats"

try:
    resp = requests.get(url, auth=(F5_USER, F5_PASS), verify=False).json()
    entries = resp.get('entries', {})
    
    total_members = len(entries)
    active_members = 0
    
    for key, value in entries.items():
        avail = value['nestedStats']['entries']['status.availabilityState']['description']
        if avail == 'available': active_members += 1
        
    print(json.dumps({"total_members": total_members, "active_members": active_members}))
except Exception as e: print(json.dumps({"error": str(e)}))