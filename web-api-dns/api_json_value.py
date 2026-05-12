#!/usr/bin/env python3
# Uso: ./api_json_value.py <URL> <CHAVE_JSON>
import sys, requests
try:
    resp = requests.get(sys.argv[1], timeout=10)
    data = resp.json()
    print(data.get(sys.argv[2], "-1"))
except:
    print("-1")