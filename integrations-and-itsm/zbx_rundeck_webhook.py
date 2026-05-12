#!/usr/bin/env python3
import requests, sys, json

# URL do Webhook gerado dentro de um Job do Rundeck
RUNDECK_WEBHOOK_URL = "http://rundeck.empresa.local:4440/api/40/webhook/gerar_token_aqui"

HOST_TARGET = sys.argv[1]
EVENT_ID = sys.argv[2]

# Enviamos o target_node para o Rundeck saber em qual máquina executar os comandos
payload = {
    "target_node": HOST_TARGET,
    "zabbix_event_id": EVENT_ID,
    "source": "Zabbix Auto-Remediation"
}

try:
    resp = requests.post(
        RUNDECK_WEBHOOK_URL,
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    resp.raise_for_status()
    print("Runbook acionado no Rundeck com sucesso.")
except Exception as e:
    print(f"Falha ao acionar Rundeck: {e}")