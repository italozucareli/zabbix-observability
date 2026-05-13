#!/usr/bin/env python3
import requests, json, sys

VAULT_ADDR, TOKEN, PKI_PATH = sys.argv[1], sys.argv[2], sys.argv[3] # Ex: pki/
headers = {"X-Vault-Token": TOKEN}

try:
    resp = requests.request("LIST", f"{VAULT_ADDR}/v1/{PKI_PATH}certs", headers=headers, verify=False).json()
    certs = resp.get('data', {}).get('keys', [])
    zbx_data = [{"{#CERT_SERIAL}": serial} for serial in certs]
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))