#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

try:
    #builtin:billing.ddu.metrics.total
    metric_selector = "builtin:billing.ddu.metrics.total:sum"
    url = f"{TENANT_URL}/api/v2/metrics/query?metricSelector={metric_selector}&timeframe=now-1h"
    
    resp = requests.get(url, headers=headers)
    data = resp.json().get('result', [])
    
    ddu_consumed = 0
    if data and data[0].get('data'):
        values = [v for v in data[0]['data'][0].get('values', []) if v is not None]
        ddu_consumed = values[-1] if values else 0
        
    print(json.dumps({"ddu_consumed_last_hour": ddu_consumed}))
except Exception as e:
    print(json.dumps({"error": str(e)}))