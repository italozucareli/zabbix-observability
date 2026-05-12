#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
HOST = sys.argv[1]
ACTION_DESC = sys.argv[2]

payload = {
    "type": "Standard",
    "short_description": f"[Zabbix Auto-Remediation] Executando ação no {HOST}",
    "description": f"O Zabbix iniciou um script automatizado: {ACTION_DESC}",
    "justification": "Correção automática baseada em threshold de monitoramento atingido.",
    "cmdb_ci": HOST
}

try:
    resp = requests.post(f"{SNOW_INSTANCE}/api/now/table/change_request", auth=AUTH, json=payload)
    resp.raise_for_status()
    print(f"Change Request criada: {resp.json().get('result', {}).get('number')}")
except Exception as e:
    print(f"Erro ao criar Change: {e}")