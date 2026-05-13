#!/usr/bin/env python3
import requests, json, sys

CONTROLLER_URL = sys.argv[1]
APP_ID = sys.argv[2]
AUTH = ("api_user@account", "api_pass")

try:
    # time-range-type=BEFORE_NOW & duration-in-mins=15
    url = f"{CONTROLLER_URL}/controller/rest/applications/{APP_ID}/problems/healthrule-violations?time-range-type=BEFORE_NOW&duration-in-mins=15&output=JSON"
    resp = requests.get(url, auth=AUTH)
    violations = resp.json()
    
    # Filtra apenas as violações que ainda não foram resolvidas
    active_violations = [v for v in violations if v.get('incidentStatus') == 'OPEN']
    
    zabbix_data = {
        "active_violations_count": len(active_violations),
        "critical_count": len([v for v in active_violations if v.get('severity') == 'CRITICAL']),
        "warning_count": len([v for v in active_violations if v.get('severity') == 'WARNING'])
    }
    
    print(json.dumps(zabbix_data, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))