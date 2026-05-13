#!/usr/bin/env python3
import requests, json, sys, datetime

F5_HOST, F5_USER, F5_PASS = sys.argv[1], sys.argv[2], sys.argv[3]
url = f"https://{F5_HOST}/mgmt/tm/sys/crypto/cert"

try:
    resp = requests.get(url, auth=(F5_USER, F5_PASS), verify=False).json()
    zbx_data = []
    for c in resp.get('items', []):
        exp_str = c.get('expirationString') # Formato: 'Oct 15 23:59:59 2024 GMT'
        if exp_str:
            exp_date = datetime.datetime.strptime(exp_str, '%b %d %H:%M:%S %Y %Z')
            days_left = (exp_date - datetime.datetime.now()).days
            zbx_data.append({"{#CERT_NAME}": c['name'], "{#DAYS_LEFT}": days_left})
            
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))