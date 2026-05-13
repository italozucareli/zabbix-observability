#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/api/alertmanager/grafana/api/v2/silences", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    zbx_data = [{"{#SILENCE_ID}": s['id'], "{#SILENCE_COMMENT}": s.get('comment', 'None')} for s in resp if s['status']['state'] == 'active']
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))