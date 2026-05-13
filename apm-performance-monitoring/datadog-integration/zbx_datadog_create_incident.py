#!/usr/bin/env python3
import requests, sys

DD_SITE, DD_API_KEY, DD_APP_KEY = sys.argv[1], sys.argv[2], sys.argv[3]
TITLE, IMPACT = sys.argv[4], sys.argv[5] # IMPACT: 1 (High) a 5 (Low)

url = f"https://api.{DD_SITE}/api/v2/incidents"
headers = {"DD-API-KEY": DD_API_KEY, "DD-APPLICATION-KEY": DD_APP_KEY, "Content-Type": "application/json"}

payload = {
    "data": {
        "type": "incidents",
        "attributes": {
            "title": f"[Zabbix] {TITLE}",
            "customer_impacted": True,
            "severity": f"SEV-{IMPACT}"
        }
    }
}
try:
    requests.post(url, headers=headers, json=payload, verify=False)
except Exception as e: print(e)