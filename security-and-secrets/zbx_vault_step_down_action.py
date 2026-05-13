#!/usr/bin/env python3
import requests, sys

VAULT_ADDR, TOKEN = sys.argv[1], sys.argv[2]
headers = {"X-Vault-Token": TOKEN}

try:
    requests.put(f"{VAULT_ADDR}/v1/sys/step-down", headers=headers, verify=False)
    print("Step-down initiated")
except Exception as e: print(e)