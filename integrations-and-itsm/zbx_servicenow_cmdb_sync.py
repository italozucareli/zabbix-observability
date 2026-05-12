#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")

HOST = sys.argv[1]
IP_ADDRESS = sys.argv[2]
OS_TYPE = sys.argv[3] # Linux ou Windows

# Define a tabela correta da CMDB baseada no SO
table = "cmdb_ci_linux_server" if "Linux" in OS_TYPE else "cmdb_ci_win_server"

payload = {
    "name": HOST,
    "ip_address": IP_ADDRESS,
    "operational_status": "1", # Operational
    "discovery_source": "Zabbix"
}

try:
    resp = requests.post(f"{SNOW_INSTANCE}/api/now/table/{table}", auth=AUTH, json=payload)
    print(f"CI cadastrado/atualizado na CMDB: {resp.json().get('result', {}).get('sys_id')}")
except Exception as e:
    print(f"Erro no CMDB Sync: {e}")