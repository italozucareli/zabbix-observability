#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/api/v1/events?fieldSelector=involvedObject.kind=HorizontalPodAutoscaler", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    scale_ups = len([e for e in resp.json().get('items', []) if e.get('reason') == 'SuccessfulRescale'])
    print(json.dumps({"recent_scale_events": scale_ups}))
except Exception as e: print(json.dumps({"error": str(e)}))