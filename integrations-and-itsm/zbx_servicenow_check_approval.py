#!/usr/bin/env python3
import requests, sys, json

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
SYSAPPROVAL_ID = sys.argv[1] # sys_id do documento aguardando aprovação (ex: Change Request)

try:
    url = f"{SNOW_INSTANCE}/api/now/table/sysapproval_approver?sysparm_query=sysapproval={SYSAPPROVAL_ID}^state=approved"
    resp = requests.get(url, auth=AUTH)
    approvals = resp.json().get('result', [])
    
    if len(approvals) > 0:
        print(json.dumps({"is_approved": 1}))
    else:
        print(json.dumps({"is_approved": 0}))
except Exception as e:
    print(json.dumps({"error": str(e)}))