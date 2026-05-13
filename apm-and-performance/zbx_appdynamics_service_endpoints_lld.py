#!/usr/bin/env python3
import requests, json, sys

CONTROLLER_URL = sys.argv[1]
APP_ID = sys.argv[2]
TIER_ID = sys.argv[3]
AUTH = ("api_user@account", "api_pass")

try:
    url = f"{CONTROLLER_URL}/controller/rest/applications/{APP_ID}/tiers/{TIER_ID}/service-endpoints?output=JSON"
    resp = requests.get(url, auth=AUTH)
    endpoints = resp.json()
    
    zabbix_data = [{"{#ENDPOINT_NAME}": ep['name'], "{#ENDPOINT_TYPE}": ep['type']} for ep in endpoints]
    
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))