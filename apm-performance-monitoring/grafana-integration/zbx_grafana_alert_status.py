#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, ALERT_UID = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/api/prometheus/grafana/api/v1/alerts", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    state = "Normal"
    for a in resp.get('data', {}).get('alerts', []):
        if a['annotations'].get('__uid__') == ALERT_UID:
            state = a['state']
            break
    print(json.dumps({"alert_state": state}))
except Exception as e: print(json.dumps({"error": str(e)}))