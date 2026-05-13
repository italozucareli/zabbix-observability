#!/usr/bin/env python3
import requests, json, sys, datetime

DD_SITE, DD_API_KEY, DD_APP_KEY = sys.argv[1], sys.argv[2], sys.argv[3]

# Pega o mês atual
start_month = datetime.datetime.now().strftime('%Y-%m-01T00:00:00Z')

url = f"https://api.{DD_SITE}/api/v1/usage/summary?start_month={start_month}"
headers = {"DD-API-KEY": DD_API_KEY, "DD-APPLICATION-KEY": DD_APP_KEY}

try:
    resp = requests.get(url, headers=headers, verify=False).json()
    usage = resp.get('usage', [{}])[0]
    
    print(json.dumps({
        "apm_host_top99p": usage.get('apm_host_top99p', 0),
        "container_hwm": usage.get('container_hwm', 0),
        "indexed_events_count": usage.get('indexed_events_count', 0)
    }, indent=2))
except Exception as e: print(json.dumps({"error": str(e)}))