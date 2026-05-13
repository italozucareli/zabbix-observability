#!/usr/bin/env python3
import requests, json, sys

VAULT_ADDR, TOKEN = sys.argv[1], sys.argv[2]
headers = {"X-Vault-Token": TOKEN}

try:
    resp = requests.get(f"{VAULT_ADDR}/v1/sys/audit", headers=headers, verify=False).json()
    # Verifica se há pelo menos um dispositivo de auditoria ativo
    print(json.dumps({"audit_devices_active": len(resp) if isinstance(resp, dict) and not resp.get('errors') else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))