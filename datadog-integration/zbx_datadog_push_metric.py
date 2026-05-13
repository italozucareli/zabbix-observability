#!/usr/bin/env python3
import requests, sys, time

DD_SITE, DD_API_KEY = sys.argv[1], sys.argv[2]
METRIC_NAME, METRIC_VALUE, HOST = sys.argv[3], sys.argv[4], sys.argv[5]

url = f"https://api.{DD_SITE}/api/v2/series"
headers = {"DD-API-KEY": DD_API_KEY, "Content-Type": "application/json"}

payload = {
    "series": [{
        "metric": f"zabbix.{METRIC_NAME}",
        "type": 3, # 3 = gauge
        "points": [{"timestamp": int(time.time()), "value": float(METRIC_VALUE)}],
        "resources": [{"type": "host", "name": HOST}]
    }]
}
try:
    requests.post(url, headers=headers, json=payload, verify=False)
except: pass