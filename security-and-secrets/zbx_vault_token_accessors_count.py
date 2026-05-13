#!/usr/bin/env python3
import requests, json, sys

VAULT_ADDR, TOKEN = sys.argv[1], sys.argv[2]
headers = {"X-Vault-Token": TOKEN}

try:
    # A API LIST em accessors retorna os IDs, usamos o length
    resp = requests.request("LIST", f"{VAULT_ADDR}/v1/auth/token/accessors", headers=headers, verify=False).json()
    keys = resp.get('data', {}).get('keys', [])
    print(json.dumps({"active_tokens_count": len(keys)}))
except Exception as e: print(json.dumps({"error": str(e)}))