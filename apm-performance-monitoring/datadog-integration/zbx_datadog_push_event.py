#!/usr/bin/env python3
import requests, json, sys

DD_SITE = sys.argv[1] # Ex: datadoghq.com ou datadoghq.eu
DD_API_KEY = sys.argv[2]
HOST = sys.argv[3]
TITLE = sys.argv[4]
TEXT = sys.argv[5]
SEVERITY = sys.argv[6] # error, warning, info, success

url = f"https://api.{DD_SITE}/api/v1/events"
headers = {"DD-API-KEY": DD_API_KEY, "Content-Type": "application/json"}

payload = {
    "title": f"[Zabbix] {TITLE}",
    "text": TEXT,
    "host": HOST,
    "alert_type": SEVERITY,
    "source_type_name": "zabbix",
    "tags": ["source:zabbix", f"host:{HOST}"]
}

try:
    requests.post(url, headers=headers, json=payload, verify=False)
    print("OK")
except Exception as e: print(e)