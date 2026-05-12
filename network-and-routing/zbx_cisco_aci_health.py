#!/usr/bin/env python3
import requests, json, sys
requests.packages.urllib3.disable_warnings()

APIC_IP = sys.argv[1]
USER = sys.argv[2]
PASS = sys.argv[3]

# 1. Login e captura do Token
auth_url = f"https://{APIC_IP}/api/aaaLogin.json"
auth_payload = {"aaaUser": {"attributes": {"name": USER, "pwd": PASS}}}
try:
    session = requests.Session()
    resp = session.post(auth_url, json=auth_payload, verify=False, timeout=10)
    resp.raise_for_status()
    
    # 2. Coleta de Falhas (Faults) no nível do Fabric
    fault_url = f"https://{APIC_IP}/api/node/class/faultSummary.json"
    faults_resp = session.get(fault_url, verify=False)
    data = faults_resp.json()
    
    zabbix_data = []
    for item in data['imdata']:
        attr = item['faultSummary']['attributes']
        zabbix_data.append({
            "{#DOMAIN}": attr['domain'],
            "{#SEVERITY}": attr['severity'],
            "count": attr['count']
        })
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))