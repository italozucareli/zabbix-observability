#!/usr/bin/env python3
import requests, sys, json

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
HOST_CI_SYS_ID = sys.argv[1]

try:
    # Query: Busca relacionamentos onde a "Criança" (child) é o nosso Host
    url = f"{SNOW_INSTANCE}/api/now/table/cmdb_rel_ci?sysparm_query=child={HOST_CI_SYS_ID}"
    resp = requests.get(url, auth=AUTH)
    relations = resp.json().get('result', [])
    
    services = []
    for rel in relations:
        parent_name = rel['parent']['link'] # Na prática, você faria um novo GET aqui ou usaria sysparm_display_value
        services.append("Business_Service_Found")
        
    print(json.dumps({"business_services_impacted": len(services)}))
except Exception as e:
    print(json.dumps({"error": str(e)}))