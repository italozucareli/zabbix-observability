#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]
APP_ID = sys.argv[3] # Ex: APPLICATION-EA7C4B...

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

try:
    #builtin:apps.web.apdex.userType
    metric_selector = f"builtin:apps.web.apdex.userType:filter(eq(dt.entity.application,{APP_ID})):avg"
    url = f"{TENANT_URL}/api/v2/metrics/query?metricSelector={metric_selector}&resolution=5m"
    
    resp = requests.get(url, headers=headers)
    data = resp.json().get('result', [])
    
    apdex = 0
    if data and data[0].get('data'):
        values = [v for v in data[0]['data'][0].get('values', []) if v is not None]
        apdex = round(values[-1], 2) if values else 0
        
    print(json.dumps({"apdex_score": apdex}))
except Exception as e:
    print(json.dumps({"error": str(e)}))