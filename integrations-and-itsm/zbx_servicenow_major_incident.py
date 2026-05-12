#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
SYS_ID = sys.argv[1] # sys_id do incidente existente
ACTION = "promote" # ou "propose"

try:
    # A API do MIM exige um endpoint específico ou atualização de campos específicos
    payload = {
        "major_incident_state": "accepted" if ACTION == "promote" else "proposed",
        "work_notes": "[Zabbix] Promovendo para Major Incident devido à queda massiva de infraestrutura."
    }
    resp = requests.patch(f"{SNOW_INSTANCE}/api/now/table/incident/{SYS_ID}", auth=AUTH, json=payload)
    resp.raise_for_status()
    print("Incidente promovido a Major Incident com sucesso.")
except Exception as e:
    print(f"Erro ao escalar para Major Incident: {e}")