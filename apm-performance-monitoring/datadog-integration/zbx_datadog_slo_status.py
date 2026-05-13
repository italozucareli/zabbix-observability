#!/usr/bin/env python3
import requests, json, sys

DD_SITE, DD_API_KEY, DD_APP_KEY, SLO_ID = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

url = f"https://api.{DD_SITE}/api/v1/slo/{SLO_ID}/history?from_ts=0&to_ts=0" # Timeframes default da API
headers = {"DD-API-KEY": DD_API_KEY, "DD-APPLICATION-KEY": DD_APP_KEY}

try:
    resp = requests.get(url, headers=headers, verify=False).json()
    data = resp.get('data', {}).get('overall', {})
    
    print(json.dumps({
        "sli_value_percent": data.get('sli_value', 0),
        "error_budget_remaining": data.get('error_budget_remaining', 0)
    }))
except Exception as e: print(json.dumps({"error": str(e)}))