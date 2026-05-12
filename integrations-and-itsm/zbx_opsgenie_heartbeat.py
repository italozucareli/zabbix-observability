#!/usr/bin/env python3
import requests

# URL do Heartbeat configurado previamente no Opsgenie
HEARTBEAT_NAME = "Zabbix-Server-Principal"
API_KEY = "sua_genie_key"
OPSGENIE_URL = f"https://api.opsgenie.com/v2/heartbeats/{HEARTBEAT_NAME}/ping"

headers = {"Authorization": f"GenieKey {API_KEY}"}

try:
    resp = requests.post(OPSGENIE_URL, headers=headers)
    resp.raise_for_status()
    print("Heartbeat enviado com sucesso para o Opsgenie.")
except Exception as e:
    print(f"Falha ao enviar Heartbeat: {e}")