#!/usr/bin/env python3
import requests, json, sys, hashlib
API_URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{API_URL}/api/v1/namespaces/kube-system/configmaps/coredns", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False)
    corefile = resp.json().get('data', {}).get('Corefile', '')
    md5_hash = hashlib.md5(corefile.encode()).hexdigest()
    print(json.dumps({"coredns_hash": md5_hash}))
except Exception as e: print(json.dumps({"error": str(e)}))