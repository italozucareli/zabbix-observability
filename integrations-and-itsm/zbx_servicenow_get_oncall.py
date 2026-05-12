#!/usr/bin/env python3
import requests, sys, json

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
GROUP_SYS_ID = sys.argv[1] # sys_id do grupo de suporte no SNOW

try:
    # Utiliza a API do módulo On-Call Scheduling do ServiceNow
    url = f"{SNOW_INSTANCE}/api/sn_on_call/v1/escalation/plan?group_id={GROUP_SYS_ID}"
    resp = requests.get(url, auth=AUTH)
    data = resp.json().get('result', {})
    
    # Extrai o contato principal atual do JSON
    primary_contact = data.get('escalation_plan', [])[0].get('roster', {}).get('primary', {}).get('email', 'N/A')
    
    print(json.dumps({"oncall_email": primary_contact}))
except Exception as e:
    print(json.dumps({"error": str(e)}))