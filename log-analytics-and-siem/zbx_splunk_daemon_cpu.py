#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/services/server/status/resource-usage/hostwide?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    cpu = resp['entry'][0]['content'].get('cpu_system_pct', 0) + resp['entry'][0]['content'].get('cpu_user_pct', 0)
    print(json.dumps({"splunkd_cpu_percent": round(cpu, 2)}))
except Exception as e: print(json.dumps({"error": str(e)}))