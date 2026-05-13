#!/usr/bin/env python3
import requests, json, sys

CONTROLLER_URL = sys.argv[1]
APP_ID = sys.argv[2]
AUTH = ("api_user@account", "api_pass")

try:
    # A API não lista Information Points diretamente via GET simples, mas podemos buscá-los pela árvore de métricas
    url = f"{CONTROLLER_URL}/controller/rest/applications/{APP_ID}/metrics?metric-path=Information%20Points&output=JSON"
    resp = requests.get(url, auth=AUTH)
    info_points = resp.json()
    
    zabbix_data = [{"{#INFO_POINT_NAME}": ip['name']} for ip in info_points if ip['type'] == 'folder']
    
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))