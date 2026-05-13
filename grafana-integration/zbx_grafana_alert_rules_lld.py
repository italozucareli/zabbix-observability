#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/api/ruler/grafana/api/v1/rules", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    zbx_data = []
    for folder, groups in resp.items():
        for g in groups:
            for r in g.get('rules', []):
                zbx_data.append({"{#ALERT_TITLE}": r['grafana_alert']['title'], "{#ALERT_UID}": r['grafana_alert']['uid']})
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))