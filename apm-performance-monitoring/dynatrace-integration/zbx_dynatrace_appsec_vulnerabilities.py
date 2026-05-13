#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json"}

try:
    # Busca Security Problems abertos
    url = f"{TENANT_URL}/api/v2/securityProblems?status=OPEN"
    resp = requests.get(url, headers=headers)
    problems = resp.json().get('securityProblems', [])
    
    critical = len([p for p in problems if p.get('riskAssessment', {}).get('riskLevel') == 'CRITICAL'])
    high = len([p for p in problems if p.get('riskAssessment', {}).get('riskLevel') == 'HIGH'])
    
    print(json.dumps({
        "total_open_vulnerabilities": len(problems),
        "critical_risk_count": critical,
        "high_risk_count": high
    }, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))