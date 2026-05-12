#!/usr/bin/env python3
import requests, json

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")

try:
    # Consulta a tabela de Hardware excluindo os que não tem garantia preenchida
    url = f"{SNOW_INSTANCE}/api/now/table/alm_hardware?sysparm_query=warranty_expirationISNOTEMPTY"
    resp = requests.get(url, auth=AUTH)
    assets = resp.json().get('result', [])
    
    zabbix_data = []
    for asset in assets:
        zabbix_data.append({
            "{#ASSET_TAG}": asset.get('asset_tag', 'unknown'),
            "{#DISPLAY_NAME}": asset.get('display_name', 'unknown'),
            "{#WARRANTY_EXP}": asset.get('warranty_expiration', '')
        })
        
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))