#!/usr/bin/env python3
import requests, json, sys

NETBOX_URL = "https://netbox.empresa.local/api/dcim/devices/?status=active"
NETBOX_TOKEN = "seu_token_netbox"
ZABBIX_URL = "https://zabbix.empresa.local/api_jsonrpc.php"
ZABBIX_TOKEN = "seu_token_api_zabbix" # Zabbix 6.0+ usa Bearer Token
GROUP_ID = "2" # ID do Host Group no Zabbix

try:
    # 1. Busca dispositivos no NetBox
    headers_nb = {"Authorization": f"Token {NETBOX_TOKEN}", "Accept": "application/json"}
    resp_nb = requests.get(NETBOX_URL, headers=headers_nb, verify=False)
    devices = resp_nb.json().get('results', [])

    # 2. Prepara chamada para o Zabbix
    headers_zbx = {"Content-Type": "application/json", "Authorization": f"Bearer {ZABBIX_TOKEN}"}
    
    for dev in devices:
        hostname = dev['name']
        ip = dev['primary_ip']['address'].split('/')[0] if dev.get('primary_ip') else None
        
        if not ip: continue

        # Payload para criar Host no Zabbix
        zbx_payload = {
            "jsonrpc": "2.0",
            "method": "host.create",
            "params": {
                "host": hostname,
                "interfaces": [{"type": 1, "main": 1, "useip": 1, "ip": ip, "dns": "", "port": "10050"}],
                "groups": [{"groupid": GROUP_ID}]
            },
            "id": 1
        }
        
        # Tenta criar (vai falhar se já existir, o que é seguro)
        requests.post(ZABBIX_URL, headers=headers_zbx, json=zbx_payload, verify=False)
        
    print("Sincronização NetBox -> Zabbix concluída com sucesso.")
except Exception as e:
    print(f"Erro na sincronização: {e}")