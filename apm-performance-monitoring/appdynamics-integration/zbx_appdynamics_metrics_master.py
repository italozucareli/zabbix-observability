#!/usr/bin/env python3
import requests, json, sys

# Configurações do Controller
CONTROLLER_URL = "https://sua-instancia.saas.appdynamics.com"
ACCOUNT_NAME = "customer1"
CLIENT_ID = "zabbix-api-client"
CLIENT_SECRET = "sua-secret"
APP_NAME = sys.argv[1] # Nome da aplicação no AppD

def get_token():
    auth_url = f"{CONTROLLER_URL}/controller/auth/v1/oauth/token"
    data = {"grant_type": "client_credentials", "client_id": f"{CLIENT_ID}@{ACCOUNT_NAME}", "client_secret": CLIENT_SECRET}
    r = requests.post(auth_url, data=data)
    return r.json()['access_token']

try:
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    # Busca métricas principais
    metric_path = "Overall Application Performance|*"
    url = f"{CONTROLLER_URL}/controller/rest/applications/{APP_NAME}/metric-data?metric-path={metric_path}&time-range-type=BEFORE_NOW&duration-in-mins=5&output=JSON"
    
    resp = requests.get(url, headers=headers)
    metrics = resp.json()
    
    result = {}
    for m in metrics:
        name = m['metricName'].split('|')[-1].lower().replace(' ', '_')
        val = m['metricValues'][0]['value'] if m['metricValues'] else 0
        result[name] = val
        
    print(json.dumps(result, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))