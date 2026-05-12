#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
HOST = sys.argv[1]
CVE_ID = sys.argv[2] # Ex: CVE-2021-44228 (Log4j)

payload = {
    "cmdb_ci": HOST,
    "vulnerability": CVE_ID,
    "state": "1", # Open
    "source": "Zabbix Security Audit",
    "short_description": f"Vulnerabilidade {CVE_ID} detectada no host {HOST}"
}

try:
    resp = requests.post(f"{SNOW_INSTANCE}/api/now/table/sn_vul_vulnerable_item", auth=AUTH, json=payload)
    print(f"Item de Vulnerabilidade criado: {resp.json().get('result', {}).get('number')}")
except Exception as e:
    print(f"Erro SecOps API: {e}")