#!/usr/bin/env python3
import requests, json, sys
requests.packages.urllib3.disable_warnings()

IP = sys.argv[1]
USER = sys.argv[2]
PASS = sys.argv[3]

try:
    # 1. Autenticação e Token
    session = requests.Session()
    session.verify = False
    auth_resp = session.post(f"https://{IP}/api/v1/security/login", json={"username": USER, "password": PASS}, timeout=10)
    auth_resp.raise_for_status()
    
    # 2. Coleta de Métricas do UPS
    data_resp = session.get(f"https://{IP}/api/v1/ups/status")
    data_resp.raise_for_status()
    ups_status = data_resp.json()
    
    # Faz logout para não travar o limite de sessões do NMC
    session.post(f"https://{IP}/api/v1/security/logout")
    
    print(json.dumps(ups_status, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))