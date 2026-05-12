#!/usr/bin/env python3
import requests, json, sys

ZABBIX_URL = sys.argv[1] 
TOKEN = sys.argv[2]      

headers = {'Content-Type': 'application/json'}

payload = {
    "jsonrpc": "2.0",
    "method": "queue.get",
    "params": {},
    "id": 1,
    "auth": TOKEN
}

try:
    resp = requests.post(ZABBIX_URL, headers=headers, json=payload, timeout=15)
    resp.raise_for_status()
    queue_data = resp.json().get('result', [])
    
    metrics = {
        "delayed_under_1m": 0,
        "delayed_1m_to_5m": 0,
        "delayed_5m_to_10m": 0,
        "delayed_over_10m": 0
    }
    
    for item in queue_data:
        delay = int(item.get('delay', 0))
        if delay < 60:
            metrics["delayed_under_1m"] += 1
        elif 60 <= delay < 300:
            metrics["delayed_1m_to_5m"] += 1
        elif 300 <= delay < 600:
            metrics["delayed_5m_to_10m"] += 1
        else:
            metrics["delayed_over_10m"] += 1
            
    print(json.dumps(metrics))
except Exception as e:
    print(json.dumps({"error": str(e)}))