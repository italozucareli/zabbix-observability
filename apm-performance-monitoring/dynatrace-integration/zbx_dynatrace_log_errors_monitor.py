#!/usr/bin/env python3
import requests, json, sys

TENANT_URL = sys.argv[1]
API_TOKEN = sys.argv[2]
HOST_ID = sys.argv[3] # dt.entity.host
SEARCH_TERM = "Exception OR Error OR FATAL"

headers = {"Authorization": f"Api-Token {API_TOKEN}", "Content-Type": "application/json"}

try:
    # DQL (Dynatrace Query Language)
    query = f'fetch logs | filter dt.entity.host == "{HOST_ID}" | filter matchesPhrase(content, "{SEARCH_TERM}") | summarize count()'
    
    payload = {
        "query": query,
        "defaultTimeframeStart": "now-15m",
        "defaultTimeframeEnd": "now"
    }
    
    url = f"{TENANT_URL}/api/v3/bizevents/query" # Execução de query DQL
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    
    result_data = resp.json()
    error_count = result_data[0].get('count()', 0) if result_data else 0
    
    print(json.dumps({"log_error_matches": error_count}))
except Exception as e:
    print(json.dumps({"error": str(e)}))