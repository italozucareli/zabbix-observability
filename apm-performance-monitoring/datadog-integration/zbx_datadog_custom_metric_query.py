#!/usr/bin/env python3
import requests, json, sys, time

DD_SITE, DD_API_KEY, DD_APP_KEY, QUERY = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

# Pega os últimos 5 minutos
now = int(time.time())
from_ts = now - 300

url = f"https://api.{DD_SITE}/api/v1/query?from={from_ts}&to={now}&query={QUERY}"
headers = {"DD-API-KEY": DD_API_KEY, "DD-APPLICATION-KEY": DD_APP_KEY}

try:
    resp = requests.get(url, headers=headers, verify=False).json()
    series = resp.get('series', [])
    
    if series and series[0].get('pointlist'):
        # Retorna o último valor [timestamp, value]
        last_val = series[0]['pointlist'][-1][1]
        print(json.dumps({"query_result": last_val}))
    else:
        print(json.dumps({"query_result": 0}))
except Exception as e: print(json.dumps({"error": str(e)}))