#!/usr/bin/env python3
import requests, json, sys
import xml.etree.ElementTree as ET

PAN_HOST, PAN_KEY, VR_NAME = sys.argv[1], sys.argv[2], sys.argv[3] # Ex VR_NAME: default
url = f"https://{PAN_HOST}/api/?type=op&cmd=<show><routing><protocol><bgp><peer><virtual-router>{VR_NAME}</virtual-router></peer></bgp></protocol></routing></show>&key={PAN_KEY}"

try:
    resp = requests.get(url, verify=False)
    root = ET.fromstring(resp.content)
    zbx_data = []
    for peer in root.findall('.//entry'):
        peer_name = peer.find('peer').text
        status = peer.find('status').text
        zbx_data.append({"{#PEER_NAME}": peer_name, "{#PEER_STATUS}": status})
        
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))