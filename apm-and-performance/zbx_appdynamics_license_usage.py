#!/usr/bin/env python3
import requests, json, sys

CONTROLLER_URL = sys.argv[1]
AUTH = ("api_user@account", "api_pass")

try:
    # Métrica de licença Peak provisionada e em uso (Account level)
    metric_path = "Application Infrastructure Performance|*|Agent|App|Peak"
    url = f"{CONTROLLER_URL}/controller/rest/applications/Server%20&%20Infrastructure%20Monitoring/metric-data?metric-path={metric_path}&time-range-type=BEFORE_NOW&duration-in-mins=5&output=JSON"
    
    resp = requests.get(url, auth=AUTH)
    metrics = resp.json()
    
    usage_data = {}
    for m in metrics:
        metric_name = m['metricName'].split('|')[-1].lower() # 'provisioned' ou 'used'
        usage_data[metric_name] = m['metricValues'][0]['value'] if m['metricValues'] else 0
        
    print(json.dumps(usage_data, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))