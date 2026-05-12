#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
BUSINESS_SERVICE = sys.argv[1] # sys_id do Business Service na CMDB
MESSAGE = sys.argv[2]

payload = {
    "type": "outage", # outage, degradation, planned
    "cmdb_ci": BUSINESS_SERVICE,
    "message": MESSAGE,
    "begin": "javascript:gs.nowDateTime()"
}

try:
    resp = requests.post(f"{SNOW_INSTANCE}/api/now/table/cmdb_ci_outage", auth=AUTH, json=payload)
    print("Registro de Outage (Indisponibilidade) criado.")
except Exception as e:
    print(f"Erro ao registrar outage: {e}")