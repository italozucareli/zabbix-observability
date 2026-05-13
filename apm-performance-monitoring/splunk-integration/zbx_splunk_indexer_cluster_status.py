#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/services/cluster/master/status?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    status = resp['entry'][0]['content']
    print(json.dumps({"search_factor_met": status.get('search_factor_met', 0), "replication_factor_met": status.get('replication_factor_met', 0)}))
except Exception as e: print(json.dumps({"error": str(e)}))