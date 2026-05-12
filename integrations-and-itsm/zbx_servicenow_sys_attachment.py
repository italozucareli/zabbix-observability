#!/usr/bin/env python3
import requests, sys

SNOW_INSTANCE = "https://dev12345.service-now.com"
AUTH = ("api_user", "api_pass")
TABLE_NAME = "incident"
SYS_ID = sys.argv[1]
FILE_PATH = sys.argv[2] # Caminho do log gerado pelo Zabbix (ex: /tmp/zabbix_trace.log)

try:
    with open(FILE_PATH, 'rb') as file_data:
        headers = {
            "Content-Type": "text/plain",
            "Accept": "application/json"
        }
        url = f"{SNOW_INSTANCE}/api/now/attachment/file?table_name={TABLE_NAME}&table_sys_id={SYS_ID}&file_name=diagnostic_log.txt"
        resp = requests.post(url, auth=AUTH, headers=headers, data=file_data)
        resp.raise_for_status()
        print("Anexo inserido com sucesso no ticket.")
except Exception as e:
    print(f"Erro no upload de anexo: {e}")