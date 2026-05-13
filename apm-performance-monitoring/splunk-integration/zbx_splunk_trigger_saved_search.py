#!/usr/bin/env python3
import requests, sys
URL, TOKEN, SEARCH_NAME = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.post(f"{URL}/services/saved/searches/{SEARCH_NAME}/dispatch", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    print(resp.status_code)
except Exception as e: print(e)