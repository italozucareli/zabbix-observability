#!/usr/bin/env python3
import requests, json, sys

VAULT_ADDR, TOKEN = sys.argv[1], sys.argv[2]
headers = {"X-Vault-Token": TOKEN}

try:
    resp = requests.get(f"{VAULT_ADDR}/v1/sys/license", headers=headers, verify=False).json()
    data = resp.get('data', {})
    print(json.dumps({"is_terminating": 1 if data.get('terminating') else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))