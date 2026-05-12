#!/usr/bin/env python3
import requests, sys

PAGERDUTY_URL = "https://events.pagerduty.com/v2/enqueue"
ROUTING_KEY = "sua_routing_key_da_integration" # Integration Key

HOST = sys.argv[1]
PROBLEM = sys.argv[2]
SEVERITY = sys.argv[3] # critical, error, warning, info

# Mapeia severidade Zabbix para PagerDuty
pd_severity = "critical" if SEVERITY in ["Disaster", "High"] else "warning"

payload = {
    "routing_key": ROUTING_KEY,
    "event_action": "trigger",
    "payload": {
        "summary": f"{HOST} is DOWN: {PROBLEM}",
        "severity": pd_severity,
        "source": HOST,
        "custom_details": {
            "Trigger Description": PROBLEM,
            "Monitored By": "Zabbix"
        }
    }
}

try:
    resp = requests.post(PAGERDUTY_URL, json=payload, headers={"Content-Type": "application/json"})
    resp.raise_for_status()
    print("Evento enviado ao PagerDuty!")
except Exception as e:
    print(f"Erro no PagerDuty: {e}")