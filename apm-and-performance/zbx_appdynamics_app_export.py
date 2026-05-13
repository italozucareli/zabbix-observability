#!/usr/bin/env python3
import requests, json, sys, hashlib

CONTROLLER_URL = sys.argv[1]
APP_ID = sys.argv[2]
AUTH = ("api_user@account", "api_pass")

try:
    # Exporta o JSON completo de configuração da aplicação
    url = f"{CONTROLLER_URL}/controller/rest/applications/{APP_ID}?output=JSON"
    resp = requests.get(url, auth=AUTH)
    app_config = json.dumps(resp.json(), sort_keys=True)
    
    config_hash = hashlib.md5(app_config.encode('utf-8')).hexdigest()
    
    print(json.dumps({"config_hash": config_hash}))
except Exception as e:
    print(json.dumps({"error": str(e)}))