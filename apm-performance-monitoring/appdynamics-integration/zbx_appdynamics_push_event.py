#!/usr/bin/env python3
import requests, sys

# Params: $1=AppID, $2=Host, $3=Severity, $4=Message
APP_ID = sys.argv[1]
HOST = sys.argv[2]
SEVERITY = sys.argv[3]
MSG = sys.argv[4]

url = f"https://controller/controller/rest/applications/{APP_ID}/events"
auth = ("api_user@account", "secret")

payload = {
    "summary": f"[Zabbix Alert] {MSG}",
    "comment": f"Reported on host: {HOST}",
    "event_type": "CUSTOM",
    "custom_event_type": "ZabbixInfraAlert",
    "severity": "ERROR" if SEVERITY in ["Disaster", "High"] else "INFO"
}

requests.post(url, auth=auth, data=payload)