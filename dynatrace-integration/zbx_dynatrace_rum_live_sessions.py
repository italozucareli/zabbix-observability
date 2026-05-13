#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]
APP_ID = sys.argv[3] # ID da aplicação RUM (ex: APPLICATION-XXXX)

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

try:
    metric_selector = f"builtin:apps.web.activeSessions.total:filter(eq(dt.entity.application,{APP_ID})):sum"
    url = f"{TENANT_URL}/api/v2/metrics/query?metricSelector={metric_selector}&resolution=1m"
    
    resp = requests.get(url, headers=headers)
    data = resp.json().get('result', [])
    
    sessions = 0
    if data and data[0].get('data'):
        values = [v for v in data[0]['data'][0].get('values', []) if v is not None]
        sessions = values[-1] if values else 0
        
    print(json.dumps({"live_active_sessions": sessions}))
except Exception as e:
    print(json.dumps({"error": str(e)}))