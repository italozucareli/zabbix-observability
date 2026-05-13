#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, HEC_NAME = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    # A URL passa o HEC_NAME formatado
    resp = requests.get(f"{URL}/services/data/inputs/http/{HEC_NAME}?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    disabled = resp['entry'][0]['content']['disabled']
    print(json.dumps({"is_active": 0 if disabled else 1}))
except Exception as e: print(json.dumps({"error": str(e)}))