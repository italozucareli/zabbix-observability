#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")

HOST = sys.argv[1]
SEVERITY = sys.argv[2]
DESCRIPTION = sys.argv[3]
EVENT_ID = sys.argv[4] # {EVENT.ID} do Zabbix para correlação

# Mapeia Zabbix (Disaster, High, etc) para ITOM Severity (1=Critical, 2=Major, 3=Minor, 4=Warning, 5=Clear)
severity_map = {"Disaster": 1, "High": 2, "Average": 3, "Warning": 4, "Information": 5, "OK": 0}

payload = {
    "source": "Zabbix",
    "node": HOST,
    "resource": "Infrastructure",
    "type": "Monitoring Alert",
    "severity": severity_map.get(SEVERITY, 4),
    "description": DESCRIPTION,
    "message_key": f"ZABBIX-{EVENT_ID}" # Chave de deduplicação
}

try:
    resp = requests.post(f"{SNOW_INSTANCE}/api/now/table/em_event", auth=AUTH, json=payload, headers={"Accept": "application/json"})
    resp.raise_for_status()
    print("Evento ITOM enviado com sucesso.")
except Exception as e:
    print(f"Erro ao enviar Evento SNOW: {e}")