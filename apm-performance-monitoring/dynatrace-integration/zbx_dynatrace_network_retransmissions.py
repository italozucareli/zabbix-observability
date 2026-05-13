#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]
HOST_ID = sys.argv[3]

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

try:
    metric_selector = f"builtin:host.network.tcpRetransmissions:filter(eq(dt.entity.host,{HOST_ID})):avg"
    url = f"{TENANT_URL}/api/v2/metrics/query?metricSelector={metric_selector}"
    
    resp = requests.get(url, headers=headers)
    data = resp.json().get('result', [])
    
    retransmissions = 0
    if data and data[0].get('data'):
        values = [v for v in data[0]['data'][0].get('values', []) if v is not None]
        retransmissions = round(values[-1], 2) if values else 0
        
    print(json.dumps({"tcp_retransmission_percent": retransmissions}))
except Exception as e:
    print(json.dumps({"error": str(e)}))