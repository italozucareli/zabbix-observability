#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
CATALOG_ITEM_SYS_ID = "sys_id_do_item_no_catalogo" # Ex: Requisitar Nova Sub-rede

payload = {
    "sysparm_quantity": "1",
    "variables": {
        "motivo": "Zabbix detectou exaustão de pool DHCP > 90%",
        "urgencia": "High"
    }
}

try:
    # Endpoint específico da Service Catalog API
    url = f"{SNOW_INSTANCE}/api/sn_sc/servicecatalog/items/{CATALOG_ITEM_SYS_ID}/order_now"
    resp = requests.post(url, auth=AUTH, json=payload)
    request_number = resp.json().get('result', {}).get('request_number')
    print(f"Requisição de Catálogo gerada: {request_number}")
except Exception as e:
    print(f"Erro ao requisitar item de catálogo: {e}")