#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
SYS_ID = sys.argv[1] # sys_id do incidente

payload = {
    "state": "3", # On Hold
    "hold_reason": "3", # Awaiting Vendor
    "work_notes": "[Zabbix] Falha de rota BGP detectada. O problema está no provedor (ISP). SLA pausado temporariamente."
}

try:
    resp = requests.patch(f"{SNOW_INSTANCE}/api/now/table/incident/{SYS_ID}", auth=AUTH, json=payload)
    print("Incidente pausado e SLA congelado com sucesso.")
except Exception as e:
    print(f"Erro ao pausar incidente: {e}")