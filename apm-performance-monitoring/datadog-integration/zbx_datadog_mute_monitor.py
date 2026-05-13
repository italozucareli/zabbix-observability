#!/usr/bin/env python3
import requests, sys, time

DD_SITE, DD_API_KEY, DD_APP_KEY = sys.argv[1], sys.argv[2], sys.argv[3]
MONITOR_ID = sys.argv[4]

url = f"https://api.{DD_SITE}/api/v1/monitor/{MONITOR_ID}/mute"
headers = {"DD-API-KEY": DD_API_KEY, "DD-APPLICATION-KEY": DD_APP_KEY, "Content-Type": "application/json"}

# Muta por 15 minutos (900 segundos)
payload = {"end": int(time.time()) + 900}
try:
    requests.post(url, headers=headers, json=payload, verify=False)
except Exception as e: print(e)