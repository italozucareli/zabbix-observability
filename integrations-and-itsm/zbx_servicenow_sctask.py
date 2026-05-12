#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
HOST = sys.argv[1]
TASK_DESC = sys.argv[2]

payload = {
    "short_description": f"[Manutenção Preventiva Zabbix] {HOST}",
    "description": TASK_DESC,
    "assignment_group": "INFRA_L2", # Necessita do sys_id do grupo ou valor correspondente no seu SNOW
    "priority": "4" # Low
}

try:
    resp = requests.post(f"{SNOW_INSTANCE}/api/now/table/sc_task", auth=AUTH, json=payload)
    print(f"SCTASK criado: {resp.json().get('result', {}).get('number')}")
except Exception as e:
    print(f"Erro ao criar SCTASK: {e}")