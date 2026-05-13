#!/usr/bin/env python3
import requests, sys

# Executado como AlertScript ou External Check no Zabbix
TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]
METRIC_KEY = sys.argv[3] # Ex: custom.zabbix.room_temperature
METRIC_VALUE = sys.argv[4] # O valor numérico que o Zabbix coletou
DIMENSION_HOST = sys.argv[5] # Nome do host de origem

# A Ingest API v2 usa o padrão Line Protocol 
# Formato: metric.key,dimensao1=valor1 valor
line_protocol_payload = f"{METRIC_KEY},host={DIMENSION_HOST} {METRIC_VALUE}"

headers = {
    "Authorization": f"Api-Token {API_TOKEN}",
    "Content-Type": "text/plain; charset=utf-8"
}

try:
    ingest_url = f"{TENANT_URL}/api/v2/metrics/ingest"
    resp = requests.post(ingest_url, headers=headers, data=line_protocol_payload)
    resp.raise_for_status()
    print(f"Métrica {METRIC_KEY} = {METRIC_VALUE} injetada no Dynatrace.")
except Exception as e:
    print(f"Falha na injeção de métrica: {e}")