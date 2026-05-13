#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]
HOST_NAME = sys.argv[3] # Nome do host conforme mapeado no Dynatrace
TRIGGER_MSG = sys.argv[4]

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Content-Type": "application/json; charset=utf-8"}

# A API v2 de eventos exige que você anexe o evento a uma entidade. 
# Usaremos uma query para encontrar a entidade pelo nome antes de injetar o evento.
try:
    # 1. Encontra o EntityID do Host
    entity_url = f"{TENANT_URL}/api/v2/entities?entitySelector=type(HOST),entityName.equals({HOST_NAME})"
    ent_resp = requests.get(entity_url, headers=headers)
    entities = ent_resp.json().get('entities', [])
    
    if not entities:
        print("Host não encontrado no Dynatrace.")
        sys.exit(1)
        
    entity_id = entities[0]['entityId']
    
    # 2. Injeta o Evento
    event_payload = {
        "eventType": "CUSTOM_INFO",
        "title": "[Zabbix Alert] Infrastructure Issue",
        "timeoutMinutes": 15,
        "entitySelector": f"entityId({entity_id})",
        "properties": {
            "ZabbixMessage": TRIGGER_MSG,
            "Source": "Zabbix ITOM"
        }
    }
    
    ingest_url = f"{TENANT_URL}/api/v2/events/ingest"
    ingest_resp = requests.post(ingest_url, headers=headers, json=event_payload)
    ingest_resp.raise_for_status()
    print("Evento injetado no Dynatrace com sucesso.")
except Exception as e:
    print(f"Erro na integração Dynatrace: {e}")