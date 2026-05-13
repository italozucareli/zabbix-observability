#!/usr/bin/env python3
import requests, json, sys

VAULT_ADDR = sys.argv[1] # Ex: https://vault.empresa.com:8200
try:
    resp = requests.get(f"{VAULT_ADDR}/v1/sys/seal-status", verify=False).json()
    print(json.dumps({"is_sealed": 1 if resp.get('sealed') else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))