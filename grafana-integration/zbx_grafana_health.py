#!/usr/bin/env python3
import requests, json, sys
URL = sys.argv[1] # A rota de health não exige token
try:
    resp = requests.get(f"{URL}/api/health", verify=False).json()
    print(json.dumps({"database_status": 1 if resp.get('database') == 'ok' else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))