#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, DASH_ID = sys.argv[1], sys.argv[2], sys.argv[3] # Exige acesso na API do DB ou loop de users
# Como a API padrão lista stars por user, puxamos o dashboard e verificamos a popularidade interna (se o plugin de insights estiver ativo)
try:
    resp = requests.get(f"{URL}/api/dashboards/id/{DASH_ID}", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    print(json.dumps({"is_starred_by_admin": 1 if resp.get('meta', {}).get('isStarred') else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))