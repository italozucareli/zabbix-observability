#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, MODEL = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/services/datamodel/model/{MODEL}?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    accel = resp['entry'][0]['content']['acceleration']
    print(json.dumps({"acceleration_enabled": 1 if accel else 0}))
except Exception as e: print(json.dumps({"error": str(e)}))