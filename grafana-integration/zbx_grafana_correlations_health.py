#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, CORR_UID = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/api/datasources/correlations/{CORR_UID}", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"correlation_active": 1 if resp.get('uid') else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))