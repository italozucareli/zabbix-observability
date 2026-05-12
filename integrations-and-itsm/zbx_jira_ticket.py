#!/usr/bin/env python3
import requests, sys
from requests.auth import HTTPBasicAuth

JIRA_URL = "https://empresa.atlassian.net/rest/api/2/issue"
JIRA_USER = "zabbix@empresa.com"
JIRA_TOKEN = "seu_api_token_jira"
PROJECT_KEY = "INFRA"

HOST = sys.argv[1]
PROBLEM = sys.argv[2]

payload = {
    "fields": {
        "project": {"key": PROJECT_KEY},
        "summary": f"[Zabbix] {HOST} - {PROBLEM}",
        "description": f"Zabbix Report:\nHost: {HOST}\nIssue: {PROBLEM}",
        "issuetype": {"name": "Bug"},
        "labels": ["zabbix", "auto-generated"]
    }
}

try:
    resp = requests.post(
        JIRA_URL,
        json=payload,
        auth=HTTPBasicAuth(JIRA_USER, JIRA_TOKEN),
        headers={"Content-Type": "application/json"}
    )
    resp.raise_for_status()
    print(f"Jira Issue criada: {resp.json().get('key')}")
except Exception as e:
    print(f"Erro Jira API: {e}")