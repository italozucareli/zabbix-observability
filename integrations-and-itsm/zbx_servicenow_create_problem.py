#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
HOST = sys.argv[1]
ISSUE_SUMMARY = sys.argv[2]

payload = {
    "short_description": f"Investigação de Causa Raiz (Flapping): {HOST}",
    "description": f"O Zabbix detectou instabilidade crônica com a trigger: {ISSUE_SUMMARY}. Necessária análise aprofundada.",
    "impact": "2",
    "urgency": "2",
    "cmdb_ci": HOST
}

try:
    resp = requests.post(f"{SNOW_INSTANCE}/api/now/table/problem", auth=AUTH, json=payload)
    print(f"Registro de Problema aberto: {resp.json().get('result', {}).get('number')}")
except Exception as e:
    print(f"Erro ao abrir Problem: {e}")