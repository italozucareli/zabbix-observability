#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1] # Ex: https://abc12345.live.dynatrace.com
API_TOKEN = sys.argv[2]

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Accept": "application/json; charset=utf-8"}

try:
    url = f"{TENANT_URL}/api/v2/problems?status=OPEN"
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    problems = resp.json().get('problems', [])
    
    impact_levels = {"INFRASTRUCTURE": 0, "SERVICE": 0, "APPLICATION": 0, "ENVIRONMENT": 0, "CUSTOM_ALERT": 0}
    
    for p in problems:
        impact = p.get('impactLevel', 'ENVIRONMENT')
        if impact in impact_levels:
            impact_levels[impact] += 1
            
    impact_levels['total_active'] = len(problems)
    print(json.dumps(impact_levels, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))