#!/usr/bin/env python3
import requests, json, sys, time
HEC_URL, HEC_TOKEN, HOST, METRIC_NAME, METRIC_VALUE = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
payload = {"time": time.time(), "host": HOST, "event": "metric", "fields": {f"metric_name:{METRIC_NAME}": float(METRIC_VALUE)}}
try:
    requests.post(f"{HEC_URL}/services/collector/event", headers={"Authorization": f"Splunk {HEC_TOKEN}"}, json=payload, verify=False)
except Exception as e: pass