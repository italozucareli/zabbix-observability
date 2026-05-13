#!/usr/bin/env python3
import requests, json, sys

ORG, TOKEN = sys.argv[1], sys.argv[2]
headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

try:
    resp = requests.get(f"https://api.github.com/orgs/{ORG}/settings/billing/shared-storage", headers=headers).json()
    # Retorna em GB
    print(json.dumps({"estimated_storage_usage_gb": resp.get('estimated_paid_storage_for_month', 0)}))
except Exception as e: print(json.dumps({"error": str(e)}))