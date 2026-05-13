#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]
SERVICE_TAG = sys.argv[3] # Ex: [Environment]Production
DEPLOYMENT_VERSION = sys.argv[4] # Ex: v1.4.2

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Content-Type": "application/json"}

try:
    payload = {
        "eventType": "CUSTOM_DEPLOYMENT",
        "title": f"Deployment of {DEPLOYMENT_VERSION}",
        "deploymentName": f"Release {DEPLOYMENT_VERSION}",
        "deploymentVersion": DEPLOYMENT_VERSION,
        "deploymentProject": "Zabbix CI/CD Automation",
        "entitySelector": f"type(SERVICE),tag({SERVICE_TAG})",
        "properties": {
            "TriggeredBy": "Zabbix Pipeline Event"
        }
    }
    
    url = f"{TENANT_URL}/api/v2/events/ingest"
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    print("Evento de Deployment injetado com sucesso no Dynatrace.")
except Exception as e:
    print(f"Erro ao injetar deployment: {e}")