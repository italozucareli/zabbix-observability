#!/usr/bin/env python3
import requests, sys, json

GLPI_URL = "https://glpi.empresa.local/apirest.php"
APP_TOKEN = "seu_app_token"
USER_TOKEN = "seu_user_token"

# Zabbix params: $1=Host, $2=Trigger, $3=Severity
HOST = sys.argv[1]
TRIGGER = sys.argv[2]
SEVERITY = sys.argv[3]

headers_init = {"App-Token": APP_TOKEN, "Authorization": f"user_token {USER_TOKEN}"}

try:
    # 1. Inicia Sessão
    session_req = requests.get(f"{GLPI_URL}/initSession", headers=headers_init, verify=False)
    session_token = session_req.json().get('session_token')
    
    # 2. Cria o Ticket
    headers_post = {
        "App-Token": APP_TOKEN,
        "Session-Token": session_token,
        "Content-Type": "application/json"
    }
    
    urgency_map = {"Disaster": 5, "High": 4, "Average": 3, "Warning": 2, "Information": 1}
    
    payload = {
        "input": {
            "name": f"[Zabbix] Alerta: {HOST}",
            "content": f"O Zabbix detectou o seguinte problema:\nHost: {HOST}\nAlerta: {TRIGGER}\nSeveridade: {SEVERITY}",
            "urgency": urgency_map.get(SEVERITY, 3),
            "type": 2 # 1 = Request, 2 = Incident
        }
    }
    
    ticket_req = requests.post(f"{GLPI_URL}/Ticket", headers=headers_post, json=payload, verify=False)
    print(f"GLPI Ticket criado: {ticket_req.json().get('id')}")
    
    # 3. Encerra Sessão
    requests.get(f"{GLPI_URL}/killSession", headers=headers_post, verify=False)
except Exception as e:
    print(f"Erro na integracao GLPI: {e}")