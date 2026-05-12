#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
INCIDENT_NUMBER = sys.argv[1] # Ex: INC0010023
WORK_NOTE_TEXT = sys.argv[2]  # O texto a ser injetado (ex: output do comando top)

try:
    # Encontra o sys_id pelo número do ticket
    query_url = f"{SNOW_INSTANCE}/api/now/table/incident?sysparm_query=number={INCIDENT_NUMBER}"
    sys_id = requests.get(query_url, auth=AUTH).json().get('result', [])[0]['sys_id']
    
    # Injeta a nota
    payload = {"work_notes": f"[Zabbix Automaton]:\n{WORK_NOTE_TEXT}"}
    requests.patch(f"{SNOW_INSTANCE}/api/now/table/incident/{sys_id}", auth=AUTH, json=payload)
    print(f"Work note adicionada ao {INCIDENT_NUMBER}")
except Exception as e:
    print(f"Erro ao atualizar work note: {e}")