#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/services/data/inputs/tcp/raw?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"active_tcp_ports": len([p for p in resp.get('entry', []) if not p['content'].get('disabled')])}))
except Exception as e: print(json.dumps({"error": str(e)}))