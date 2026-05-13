#!/usr/bin/env python3
import requests, json, sys

CONTROLLER_URL = sys.argv[1]
APP_ID = sys.argv[2]
TIER_NAME = sys.argv[3]
NODE_NAME = sys.argv[4]
AUTH = ("api_user@account", "api_pass")

try:
    metric_path = f"Application Infrastructure Performance|{TIER_NAME}|Individual Nodes|{NODE_NAME}|JMX|Memory|Heap|Used %"
    url = f"{CONTROLLER_URL}/controller/rest/applications/{APP_ID}/metric-data?metric-path={metric_path}&time-range-type=BEFORE_NOW&duration-in-mins=5&output=JSON"
    
    resp = requests.get(url, auth=AUTH)
    data = resp.json()
    
    heap_used = data[0]['metricValues'][0]['value'] if data and data[0]['metricValues'] else 0
    
    print(json.dumps({"heap_used_percent": heap_used}))
except Exception as e:
    print(json.dumps({"error": str(e)}))