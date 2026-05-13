#!/usr/bin/env python3
import requests, json, sys

OWNER, REPO, TOKEN = sys.argv[1], sys.argv[2], sys.argv[3]
headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

try:
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/dependabot/alerts?state=open"
    resp = requests.get(url, headers=headers).json()
    critical = len([a for a in resp if a.get('security_vulnerability', {}).get('severity') == 'critical'])
    high = len([a for a in resp if a.get('security_vulnerability', {}).get('severity') == 'high'])
    print(json.dumps({"total_open": len(resp), "critical": critical, "high": high}))
except Exception as e: print(json.dumps({"error": str(e)}))