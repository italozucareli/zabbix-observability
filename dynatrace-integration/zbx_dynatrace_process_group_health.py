#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]
PROCESS_GROUP_ID = sys.argv[3]

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

try:
    #builtin:tech.generic.processCount
    metric_selector = f"builtin:tech.generic.processCount:filter(eq(dt.entity.process_group,{PROCESS_GROUP_ID})):sum"
    url = f"{TENANT_URL}/api/v2/metrics/query?metricSelector={metric_selector}&resolution=1m"
    
    resp = requests.get(url, headers=headers)
    data = resp.json().get('result', [])
    
    count = 0
    if data and data[0].get('data'):
        values = [v for v in data[0]['data'][0].get('values', []) if v is not None]
        count = values[-1] if values else 0
        
    print(json.dumps({"active_instances_count": count}))
except Exception as e:
    print(json.dumps({"error": str(e)}))