#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2] # Requer token de Admin global
try:
    resp = requests.get(f"{URL}/api/admin/stats", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps(resp))
except Exception as e: print(json.dumps({"error": str(e)}))