#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]
MONITOR_ID = sys.argv[3]

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

try:
    success_sel = f"builtin:synthetic.browser.successRate:filter(eq(dt.entity.synthetic_test,{MONITOR_ID})):avg"
    duration_sel = f"builtin:synthetic.browser.duration:filter(eq(dt.entity.synthetic_test,{MONITOR_ID})):avg"
    
    results = {}
    
    # Executa a query de Success Rate
    resp_succ = requests.get(f"{TENANT_URL}/api/v2/metrics/query?metricSelector={success_sel}", headers=headers)
    d_succ = resp_succ.json().get('result', [])
    if d_succ and d_succ[0].get('data'):
        vals = [v for v in d_succ[0]['data'][0].get('values', []) if v is not None]
        results["success_rate_percent"] = vals[-1] if vals else 0
        
    # Executa a query de Duration
    resp_dur = requests.get(f"{TENANT_URL}/api/v2/metrics/query?metricSelector={duration_sel}", headers=headers)
    d_dur = resp_dur.json().get('result', [])
    if d_dur and d_dur[0].get('data'):
        vals = [v for v in d_dur[0]['data'][0].get('values', []) if v is not None]
        results["duration_ms"] = vals[-1] if vals else 0

    print(json.dumps(results, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))