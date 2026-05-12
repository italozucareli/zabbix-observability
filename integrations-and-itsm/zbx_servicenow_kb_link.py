#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
INCIDENT_SYS_ID = sys.argv[1]
SEARCH_TERM = sys.argv[2] # Palavra-chave do Trigger do Zabbix

try:
    # Busca KB Articles publicados que contenham o termo no texto curto
    url = f"{SNOW_INSTANCE}/api/now/table/kb_knowledge?sysparm_query=short_descriptionLIKE{SEARCH_TERM}^workflow_state=published"
    resp = requests.get(url, auth=AUTH)
    kbs = resp.json().get('result', [])
    
    if len(kbs) > 0:
        kb_number = kbs[0]['number']
        kb_link = f"{SNOW_INSTANCE}/kb_view.do?sysparm_article={kb_number}"
        
        payload = {
            "work_notes": f"[Zabbix Assistente] Encontrei este artigo na KB que pode ajudar a resolver o problema: {kb_link}"
        }
        requests.patch(f"{SNOW_INSTANCE}/api/now/table/incident/{INCIDENT_SYS_ID}", auth=AUTH, json=payload)
        print("Link da KB injetado no incidente.")
    else:
        print("Nenhum artigo KB encontrado.")
except Exception as e:
    print(f"Erro na busca de KB: {e}")