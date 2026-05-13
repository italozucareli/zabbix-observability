#!/usr/bin/env python3
import requests, json, sys
import xml.etree.ElementTree as ET

PAN_HOST, PAN_KEY = sys.argv[1], sys.argv[2]
url = f"https://{PAN_HOST}/api/?type=op&cmd=<show><wildfire><status></status></wildfire></show>&key={PAN_KEY}"

try:
    resp = requests.get(url, verify=False)
    root = ET.fromstring(resp.content)
    status = root.find('.//connection-status').text
    print(json.dumps({"is_connected": 1 if status == 'connected' else 0, "status": status}))
except Exception as e: print(json.dumps({"error": str(e)}))