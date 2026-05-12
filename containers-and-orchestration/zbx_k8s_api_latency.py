#!/usr/bin/env python3
import requests, json, sys, time
requests.packages.urllib3.disable_warnings()

API_URL = sys.argv[1]
TOKEN = sys.argv[2]
headers = {"Authorization": f"Bearer {TOKEN}"}

try:
    start_time = time.time()
    resp = requests.get(f"{API_URL}/api/v1/namespaces", headers=headers, verify=False, timeout=10)
    resp.raise_for_status()
    end_time = time.time()
    
    latency_ms = round((end_time - start_time) * 1000, 2)
    
    print(json.dumps({
        "status": 1,
        "latency_ms": latency_ms
    }))
except Exception as e:
    print(json.dumps({"status": 0, "error": str(e)}))