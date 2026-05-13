#!/usr/bin/env python3
import requests, json, sys

CONTROLLER_URL = sys.argv[1]
AUTH = ("api_user@account", "api_pass")

try:
    url = f"{CONTROLLER_URL}/controller/rest/databases/collectors?output=JSON"
    resp = requests.get(url, auth=AUTH)
    collectors = resp.json()
    
    zabbix_data = [{"{#DB_COLLECTOR_NAME}": c['name'], "{#DB_TYPE}": c['type']} for c in collectors]
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))