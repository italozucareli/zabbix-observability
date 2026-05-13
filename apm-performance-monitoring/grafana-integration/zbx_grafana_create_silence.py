#!/usr/bin/env python3
import requests, sys, time
URL, TOKEN, MATCH_LABEL = sys.argv[1], sys.argv[2], sys.argv[3]
payload = {"matchers": [{"name": "host", "value": MATCH_LABEL, "isRegex": False}], "startsAt": time.strftime("%Y-%m-%dT%H:%M:%SZ"), "endsAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() + 3600)), "comment": "Silenced by Zabbix"}
try:
    requests.post(f"{URL}/api/alertmanager/grafana/api/v2/silences", headers={"Authorization": f"Bearer {TOKEN}"}, json=payload, verify=False)
except: pass