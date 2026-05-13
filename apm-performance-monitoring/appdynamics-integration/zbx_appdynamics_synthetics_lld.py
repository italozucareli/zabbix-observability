#!/usr/bin/env python3
import requests, json, sys

CONTROLLER_URL = sys.argv[1]
EUM_APP_ID = sys.argv[2] # O ID da aplicação EUM costuma ser diferente da aplicação APM
AUTH = ("api_user@account", "api_pass")

try:
    url = f"{CONTROLLER_URL}/controller/rest/applications/{EUM_APP_ID}/synthetic/jobs?output=JSON"
    resp = requests.get(url, auth=AUTH)
    jobs = resp.json()
    
    zabbix_data = [{"{#SYNTHETIC_JOB_NAME}": job['name'], "{#SYNTHETIC_JOB_ID}": job['id']} for job in jobs]
    
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))