#!/usr/bin/env python3
import requests, json, sys

CONTROLLER_URL = sys.argv[1]
APP_ID = sys.argv[2]
AUTH = ("user@account", "pass")

try:
    url = f"{CONTROLLER_URL}/controller/rest/applications/{APP_ID}/health-rules?output=JSON"
    resp = requests.get(url, auth=AUTH)
    rules = resp.json()
    
    zabbix_data = [{"{#RULE_NAME}": r['name'], "{#RULE_TYPE}": r['type']} for r in rules]
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))