#!/usr/bin/env python3
import requests, json, sys

VAULT_ADDR, TOKEN = sys.argv[1], sys.argv[2]
headers = {"X-Vault-Token": TOKEN}

try:
    resp = requests.get(f"{VAULT_ADDR}/v1/sys/auth", headers=headers, verify=False).json()
    zbx_data = [{"{#AUTH_PATH}": k, "{#AUTH_TYPE}": v['type']} for k, v in resp.items()]
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))