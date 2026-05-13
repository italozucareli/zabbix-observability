#!/usr/bin/env python3
import requests, sys, time
URL, TOKEN, HOST, MSG = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
payload = {"text": f"[Zabbix] {MSG}", "tags": ["zabbix", "alert", HOST], "time": int(time.time() * 1000)}
try:
    requests.post(f"{URL}/api/annotations", headers={"Authorization": f"Bearer {TOKEN}"}, json=payload, verify=False)
    print("OK")
except Exception as e: print(e)