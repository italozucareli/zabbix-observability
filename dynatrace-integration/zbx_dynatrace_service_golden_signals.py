#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]
SERVICE_ID = sys.argv[3] # Ex: SERVICE-1A2B3C4D5E

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

# Queries formatadas para API v2
metrics = {
    "response_time_ms": f"builtin:service.response.time:filter(eq(dt.entity.service,{SERVICE_ID})):avg",
    "failure_rate_percent": f"builtin:service.errors.total.rate:filter(eq(dt.entity.service,{SERVICE_ID})):avg",
    "request_count": f"builtin:service.requestCount.total:filter(eq(dt.entity.service,{SERVICE_ID})):sum"
}

results = {}

try:
    for key, metric_selector in metrics.items():
        url = f"{TENANT_URL}/api/v2/metrics/query?metricSelector={metric_selector}&resolution=5m"
        resp = requests.get(url, headers=headers)
        data = resp.json().get('result', [])
        
        if data and data[0].get('data'):
            # Pega o último valor numérico válido
            values = [v for v in data[0]['data'][0].get('values', []) if v is not None]
            results[key] = values[-1] if values else 0
        else:
            results[key] = 0
            
    print(json.dumps(results, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))