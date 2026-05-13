#!/usr/bin/env python3
import requests, json, sys

OWNER, REPO, WORKFLOW_ID, TOKEN = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

try:
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW_ID}/runs?per_page=1&branch=main"
    resp = requests.get(url, headers=headers).json()
    runs = resp.get('workflow_runs', [])
    if runs:
        conclusion = runs[0].get('conclusion')
        print(json.dumps({"last_run_failed": 1 if conclusion == 'failure' else 0}))
    else:
        print(json.dumps({"last_run_failed": 0}))
except Exception as e: print(json.dumps({"error": str(e)}))