#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN, INDEX = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    resp = requests.get(f"{URL}/services/data/indexes/{INDEX}?output_mode=json", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    size = resp['entry'][0]['content']['currentDBSizeMB']
    print(json.dumps({"size_mb": float(size)}))
except Exception as e: print(json.dumps({"error": str(e)}))