#!/usr/bin/env python3
import requests, json, sys

CONTROLLER_URL = sys.argv[1]
APP_ID = sys.argv[2]
TIER_NAME = sys.argv[3]
AUTH = ("api_user@account", "api_pass")

try:
    metric_path = f"Application Infrastructure Performance|{TIER_NAME}|*"
    url = f"{CONTROLLER_URL}/controller/rest/applications/{APP_ID}/metric-data?metric-path={metric_path}&time-range-type=BEFORE_NOW&duration-in-mins=5&output=JSON"
    
    resp = requests.get(url, auth=AUTH)
    metrics = resp.json()
    
    result = {}
    for m in metrics:
        name = m['metricName'].split('|')[-1].lower().replace(' ', '_')
        val = m['metricValues'][0]['value'] if m['metricValues'] else 0
        result[name] = val
        
    print(json.dumps(result, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))