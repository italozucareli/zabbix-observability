#!/usr/bin/env python3
import requests, json, sys
HEC_URL, HEC_TOKEN, HOST, MSG, SEVERITY = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
payload = {"host": HOST, "sourcetype": "zabbix:alert", "event": {"message": MSG, "severity": SEVERITY, "source": "Zabbix ITOM"}}
try:
    requests.post(f"{HEC_URL}/services/collector/event", headers={"Authorization": f"Splunk {HEC_TOKEN}"}, json=payload, verify=False)
    print("OK")
except Exception as e: print(f"Error: {e}")