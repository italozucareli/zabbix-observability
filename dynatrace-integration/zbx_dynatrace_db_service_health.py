#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]
DB_SERVICE_ID = sys.argv[3]

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

try:
    rt_selector = f"builtin:service.db.sql.response.time:filter(eq(dt.entity.service,{DB_SERVICE_ID})):avg"
    url = f"{TENANT_URL}/api/v2/metrics/query?metricSelector={rt_selector}"
    
    resp = requests.get(url, headers=headers)
    data = resp.json().get('result', [])
    
    sql_rt = 0
    if data and data[0].get('data'):
        values = [v for v in data[0]['data'][0].get('values', []) if v is not None]
        sql_rt = values[-1] if values else 0
        
    print(json.dumps({"sql_avg_response_time_ms": sql_rt}))
except Exception as e:
    print(json.dumps({"error": str(e)}))