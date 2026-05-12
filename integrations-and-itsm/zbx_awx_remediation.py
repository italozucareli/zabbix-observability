#!/usr/bin/env python3
# Usado como Zabbix Media Type (Webhook/Script)
import requests, sys

# Zabbix passa macros como argumentos: $1=Host, $2=TriggerName
HOST_AFFECTED = sys.argv[1]
TRIGGER_NAME = sys.argv[2]

AWX_URL = "https://awx.empresa.local/api/v2/job_templates/15/launch/"
AWX_USER = "zabbix_api"
AWX_PASS = "senha123"

# Passa o nome do host que falhou como variável extra (extra_vars) para o Ansible agir apenas nele
payload = {
    "extra_vars": {
        "target_host": HOST_AFFECTED,
        "zabbix_trigger": TRIGGER_NAME
    }
}

try:
    resp = requests.post(AWX_URL, auth=(AWX_USER, AWX_PASS), json=payload, verify=False)
    resp.raise_for_status()
    print("Job de remediação disparado no Ansible AWX com sucesso!")
except Exception as e:
    print(f"Erro ao acionar Ansible: {e}")