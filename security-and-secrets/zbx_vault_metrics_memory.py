#!/usr/bin/env python3
import requests, json, sys

VAULT_ADDR, TOKEN = sys.argv[1], sys.argv[2]
headers = {"X-Vault-Token": TOKEN}

try:
    resp = requests.get(f"{VAULT_ADDR}/v1/sys/metrics?format=json", headers=headers, verify=False).json()
    sys_mem = resp.get('sys', {}).get('runtime', {}).get('sys_bytes', 0)
    print(json.dumps({"vault_sys_memory_bytes": sys_mem}))
except Exception as e: print(json.dumps({"error": str(e)}))