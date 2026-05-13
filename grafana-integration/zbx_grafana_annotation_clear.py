#!/usr/bin/env python3
import requests, sys
URL, TOKEN, ALERT_TAG = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    requests.post(f"{URL}/api/annotations/mass-delete", headers={"Authorization": f"Bearer {TOKEN}"}, json={"tags": [ALERT_TAG]}, verify=False)
except: pass