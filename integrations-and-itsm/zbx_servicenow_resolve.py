#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
EVENT_ID = sys.argv[1] # ID do Evento original que gerou o ticket

try:
    # 1. Busca o sys_id do Incidente usando o correlation_id
    query_url = f"{SNOW_INSTANCE}/api/now/table/incident?sysparm_query=correlation_id=ZABBIX-{EVENT_ID}"
    resp_query = requests.get(query_url, auth=AUTH)
    incidents = resp_query.json().get('result', [])
    
    if incidents:
        sys_id = incidents[0]['sys_id']
        
        # 2. Atualiza o Incidente para Resolved (State=6)
        resolve_payload = {
            "state": "6",
            "close_code": "Solved (Permanently)",
            "close_notes": "Zabbix detectou a recuperação automática do serviço e resolveu o incidente.",
            "work_notes": "Trigger do Zabbix retornou para OK."
        }
        resp_patch = requests.patch(f"{SNOW_INSTANCE}/api/now/table/incident/{sys_id}", auth=AUTH, json=resolve_payload)
        resp_patch.raise_for_status()
        print(f"Incidente {incidents[0]['number']} resolvido automaticamente.")
    else:
        print("Nenhum incidente encontrado para este Evento.")
except Exception as e:
    print(f"Erro na resolução: {e}")