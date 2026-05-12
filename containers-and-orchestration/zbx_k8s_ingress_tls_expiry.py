#!/usr/bin/env python3
import requests, json, sys, base64, subprocess, datetime
from dateutil import parser # Requer: pip install python-dateutil
requests.packages.urllib3.disable_warnings()

API_URL = sys.argv[1]
TOKEN = sys.argv[2]
headers = {"Authorization": f"Bearer {TOKEN}"}

try:
    resp = requests.get(f"{API_URL}/api/v1/secrets?fieldSelector=type=kubernetes.io/tls", headers=headers, verify=False, timeout=10)
    resp.raise_for_status()
    secrets = resp.json().get('items', [])
    
    zabbix_data = []
    for sec in secrets:
        try:
            crt_b64 = sec['data']['tls.crt']
            crt_pem = base64.b64decode(crt_b64).decode('utf-8')
            
            # Passa o PEM para o OpenSSL do sistema operacional
            process = subprocess.Popen(['openssl', 'x509', '-noout', '-enddate'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, _ = process.communicate(input=crt_pem.encode('utf-8'))
            
            # Ex: notAfter=Dec 31 23:59:59 2026 GMT
            date_str = stdout.decode('utf-8').strip().split('=')[1]
            exp_date = parser.parse(date_str)
            days_left = (exp_date.replace(tzinfo=None) - datetime.datetime.utcnow()).days
            
            zabbix_data.append({
                "{#SECRET_NAME}": sec['metadata']['name'],
                "{#NAMESPACE}": sec['metadata']['namespace'],
                "days_valid": days_left
            })
        except:
            continue

    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))