#!/usr/bin/env python3
import requests, json, sys

CONTROLLER_URL = sys.argv[1]
APP_ID = sys.argv[2]
USER_PASS = ("user@account", "password") # Ou use OAuth

try:
    url = f"{CONTROLLER_URL}/controller/rest/applications/{APP_ID}/business-transactions?output=JSON"
    resp = requests.get(url, auth=USER_PASS)
    bts = resp.json()
    
    zabbix_data = [{"{#BT_NAME}": b['name'], "{#BT_ID}": b['id']} for b in bts if b['entryPointType'] != "INTERNAL"]
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))