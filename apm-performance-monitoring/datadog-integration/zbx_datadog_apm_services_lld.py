#!/usr/bin/env python3
import requests, json, sys

DD_SITE, DD_API_KEY, DD_APP_KEY = sys.argv[1], sys.argv[2], sys.argv[3]

url = f"https://api.{DD_SITE}/api/v1/service_dependencies" # Lista os serviços conectados
headers = {"DD-API-KEY": DD_API_KEY, "DD-APPLICATION-KEY": DD_APP_KEY}

try:
    resp = requests.get(url, headers=headers, verify=False).json()
    services = set()
    for edge in resp:
        services.add(edge.get('source'))
        services.add(edge.get('dest'))
        
    zbx_data = [{"{#APM_SERVICE_NAME}": s} for s in services if s]
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))