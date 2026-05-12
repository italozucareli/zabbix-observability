#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
INCIDENT_SYS_ID = sys.argv[1]
TIER3_GROUP_ID = "sys_id_do_grupo_N3"

payload = {
    "assignment_group": TIER3_GROUP_ID,
    "impact": "1",
    "urgency": "1",
    "work_notes": "[Zabbix Escalation] A trigger está ativa há mais de 4 horas sem resolução. Escalonando para Engenharia N3."
}

try:
    requests.patch(f"{SNOW_INSTANCE}/api/now/table/incident/{INCIDENT_SYS_ID}", auth=AUTH, json=payload)
    print("Incidente escalonado para Nível 3.")
except Exception as e:
    print(f"Erro ao escalonar incidente: {e}")