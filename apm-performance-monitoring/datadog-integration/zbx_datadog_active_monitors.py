#!/usr/bin/env python3
import requests, json, sys

DD_SITE, DD_API_KEY, DD_APP_KEY = sys.argv[1], sys.argv[2], sys.argv[3]

url = f"https://api.{DD_SITE}/api/v1/monitor?group_states=alert,warn"
headers = {"DD-API-KEY": DD_API_KEY, "DD-APPLICATION-KEY": DD_APP_KEY}

try:
    resp = requests.get(url, headers=headers, verify=False).json()
    alerts = len([m for m in resp if m.get('overall_state') == 'Alert'])
    warns = len([m for m in resp if m.get('overall_state') == 'Warn'])
    print(json.dumps({"active_alerts": alerts, "active_warnings": warns}))
except Exception as e: print(json.dumps({"error": str(e)}))