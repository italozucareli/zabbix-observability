#!/usr/bin/env python3
import requests, json, sys
import xml.etree.ElementTree as ET

PAN_HOST, PAN_KEY = sys.argv[1], sys.argv[2]
url = f"https://{PAN_HOST}/api/?type=op&cmd=<show><session><info></info></session></show>&key={PAN_KEY}"

try:
    resp = requests.get(url, verify=False)
    root = ET.fromstring(resp.content)
    num_active = int(root.find('.//num-active').text)
    num_max = int(root.find('.//num-max').text)
    
    utilization = round((num_active / num_max) * 100, 2) if num_max > 0 else 0
    print(json.dumps({"active_sessions": num_active, "max_sessions": num_max, "utilization_percent": utilization}))
except Exception as e: print(json.dumps({"error": str(e)}))