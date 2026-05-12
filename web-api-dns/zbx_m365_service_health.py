#!/usr/bin/env python3
import requests, json, sys

TENANT_ID = sys.argv[1]
CLIENT_ID = sys.argv[2]
CLIENT_SECRET = sys.argv[3]

token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
token_data = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "scope": "https://graph.microsoft.com/.default"
}

try:
    token_resp = requests.post(token_url, data=token_data)
    token = token_resp.json().get('access_token')
    
    health_url = "https://graph.microsoft.com/v1.0/admin/serviceAnnouncement/healthOverviews"
    headers = {"Authorization": f"Bearer {token}"}
    health_resp = requests.get(health_url, headers=headers)
    services = health_resp.json().get('value', [])
    
    zabbix_data = []
    for srv in services:
        zabbix_data.append({
            "{#SERVICE_NAME}": srv['service'],
            "status": srv['status'] 
        })
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))