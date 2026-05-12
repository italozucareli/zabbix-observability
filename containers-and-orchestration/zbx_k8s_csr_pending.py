#!/usr/bin/env python3
import requests, json, sys
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/apis/certificates.k8s.io/v1/certificatesigningrequests", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    pending = [c for c in resp.json().get('items', []) if not c.get('status', {}).get('conditions')]
    print(json.dumps({"pending_csr_count": len(pending)}))
except Exception as e: print(json.dumps({"error": str(e)}))