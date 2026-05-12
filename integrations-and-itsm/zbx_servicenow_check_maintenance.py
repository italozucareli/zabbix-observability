#!/usr/bin/env python3
import requests, sys, json

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
HOST = sys.argv[1]

try:
    # Query: Change Request está 'Implement' (state=-1) E Data Inicial <= Agora E Data Final >= Agora E CI = Host
    # Nota: A query exata depende das customizações da sua CMDB
    query = f"cmdb_ci.name={HOST}^state=-1^start_date<=javascript:gs.nowDateTime()^end_date>=javascript:gs.nowDateTime()"
    url = f"{SNOW_INSTANCE}/api/now/table/change_request?sysparm_query={query}"
    
    resp = requests.get(url, auth=AUTH)
    changes = resp.json().get('result', [])
    
    if len(changes) > 0:
        chg_num = changes[0]['number']
        # Retorna 1 (Em Manutenção) para o Zabbix tratar na Trigger ou Action
        print(json.dumps({"in_maintenance": 1, "change_ticket": chg_num}))
    else:
        print(json.dumps({"in_maintenance": 0, "change_ticket": "None"}))
except Exception as e:
    print(json.dumps({"error": str(e)}))