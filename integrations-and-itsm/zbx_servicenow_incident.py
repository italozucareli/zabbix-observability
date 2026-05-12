#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
SNOW_USER = "api_user"
SNOW_PASS = "api_pass"

# Argumentos vindos da Action do Zabbix
HOST = sys.argv[1]
SEVERITY = sys.argv[2] # Disaster, High, Average...
PROBLEM_DESC = sys.argv[3]

# Mapeia severidade do Zabbix para Urgência do ServiceNow (1=High, 2=Medium, 3=Low)
urgency_map = {"Disaster": "1", "High": "1", "Average": "2", "Warning": "3", "Information": "3"}

payload = {
    "short_description": f"[Zabbix] {HOST} - {PROBLEM_DESC}",
    "category": "Network",
    "urgency": urgency_map.get(SEVERITY, "3"),
    "impact": "2",
    "caller_id": "Zabbix Monitoring"
}

headers = {"Content-Type": "application/json", "Accept": "application/json"}

try:
    resp = requests.post(f"{SNOW_INSTANCE}/api/now/table/incident", auth=(SNOW_USER, SNOW_PASS), headers=headers, json=payload)
    resp.raise_for_status()
    ticket_num = resp.json().get('result', {}).get('number')
    print(f"Incidente {ticket_num} aberto com sucesso.")
except Exception as e:
    print(f"Falha ao abrir chamado no SNOW: {e}")