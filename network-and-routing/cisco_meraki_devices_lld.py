#!/usr/bin/env python3
import requests, sys, json
API_KEY = sys.argv[1]
NETWORK_ID = sys.argv[2]
url = f"https://api.meraki.com/api/v1/networks/{NETWORK_ID}/devices/statuses"
headers = {"X-Cisco-Meraki-API-Key": API_KEY, "Accept": "application/json"}
try:
    resp = requests.get(url, headers=headers, timeout=10)
    devices = resp.json()
    zabbix_data = [{"{#MAC}": d['mac'], "{#NAME}": d['name'], "status": d['status']} for d in devices]
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))