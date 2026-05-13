#!/usr/bin/env python3
import requests, json, sys
import xml.etree.ElementTree as ET

PAN_HOST, PAN_KEY = sys.argv[1], sys.argv[2]
url = f"https://{PAN_HOST}/api/?type=op&cmd=<show><high-availability><state></state></high-availability></show>&key={PAN_KEY}"

try:
    resp = requests.get(url, verify=False)
    root = ET.fromstring(resp.content)
    state = root.find('.//local-info/state').text
    peer_state = root.find('.//peer-info/state').text
    
    print(json.dumps({"local_state": state, "is_active": 1 if state == 'active' else 0, "peer_state": peer_state}))
except Exception as e: print(json.dumps({"error": str(e)}))