#!/usr/bin/env python3
import requests, json, sys
requests.packages.urllib3.disable_warnings()

API_URL = sys.argv[1]
TOKEN = sys.argv[2]
headers = {"Authorization": f"Bearer {TOKEN}"}

try:
    # Filtra direto na API Server para economizar banda
    url = f"{API_URL}/api/v1/events?fieldSelector=type=Warning"
    resp = requests.get(url, headers=headers, verify=False, timeout=10)
    resp.raise_for_status()
    events = resp.json().get('items', [])
    
    # Agrupa por "Reason" (ex: FailedScheduling, BackOff)
    reasons = {}
    for ev in events:
        reason = ev.get('reason', 'Unknown')
        reasons[reason] = reasons.get(reason, 0) + 1
        
    print(json.dumps({
        "total_warnings": len(events),
        "details": reasons
    }))
except Exception as e:
    print(json.dumps({"error": str(e)}))