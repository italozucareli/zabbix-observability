#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]
SLO_ID = sys.argv[3] # Ex: 1e57c251-1b22-386b-88a3-2c1b827361a9

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

try:
    url = f"{TENANT_URL}/api/v2/slo/{SLO_ID}"
    resp = requests.get(url, headers=headers)
    data = resp.json()
    
    # Extrai o valor avaliado do SLO e o Error Budget restante
    slo_value = data.get('evaluatedPercentage', 0)
    error_budget = data.get('errorBudget', 0)
    target = data.get('target', 0)
    
    print(json.dumps({
        "slo_compliance_percent": round(slo_value, 2),
        "error_budget_percent": round(error_budget, 2),
        "target_percent": target,
        "is_healthy": 1 if slo_value >= target else 0
    }, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))