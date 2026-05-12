#!/usr/bin/env python3
import requests, sys

PAGE_ID = "seu_page_id"
COMPONENT_ID = "seu_component_id" # O ID do serviço na sua Statuspage
API_TOKEN = "seu_token_atlassian"

STATUSPAGE_URL = f"https://api.statuspage.io/v1/pages/{PAGE_ID}/components/{COMPONENT_ID}"

# STATUS_TYPE: "operational", "degraded_performance", "partial_outage", "major_outage"
NEW_STATUS = sys.argv[1] 

headers = {
    "Authorization": f"OAuth {API_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "component": {
        "status": NEW_STATUS
    }
}

try:
    resp = requests.patch(STATUSPAGE_URL, headers=headers, json=payload)
    resp.raise_for_status()
    print(f"Statuspage atualizada para: {NEW_STATUS}")
except Exception as e:
    print(f"Erro ao atualizar Statuspage: {e}")