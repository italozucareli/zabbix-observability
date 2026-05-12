#!/usr/bin/env python3
import requests, json, sys, base64, gzip
requests.packages.urllib3.disable_warnings()

API_URL = sys.argv[1]
TOKEN = sys.argv[2]
headers = {"Authorization": f"Bearer {TOKEN}"}

try:
    url = f"{API_URL}/api/v1/secrets?labelSelector=owner=helm"
    resp = requests.get(url, headers=headers, verify=False, timeout=15)
    resp.raise_for_status()
    secrets = resp.json().get('items', [])
    
    zabbix_data = []
    for sec in secrets:
        try:
            # Helm v3 encoding flow: secret data -> b64decode -> b64decode -> gzip decompress -> JSON
            raw_data = sec['data']['release']
            b64_1 = base64.b64decode(raw_data)
            b64_2 = base64.b64decode(b64_1)
            release_json = json.loads(gzip.decompress(b64_2).decode('utf-8'))
            
            zabbix_data.append({
                "{#RELEASE_NAME}": release_json.get('name'),
                "{#NAMESPACE}": release_json.get('namespace'),
                "{#REVISION}": release_json.get('version'),
                "status": release_json.get('info', {}).get('status', 'unknown')
            })
        except:
            continue
            
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))