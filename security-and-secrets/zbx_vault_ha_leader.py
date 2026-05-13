#!/usr/bin/env python3
import requests, json, sys

VAULT_ADDR = sys.argv[1]
try:
    resp = requests.get(f"{VAULT_ADDR}/v1/sys/leader", verify=False).json()
    print(json.dumps({"is_active_leader": 1 if resp.get('is_self') else 0, "ha_enabled": 1 if resp.get('ha_enabled') else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))