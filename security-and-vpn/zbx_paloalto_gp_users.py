#!/usr/bin/env python3
import requests, xml.etree.ElementTree as ET, json, sys
requests.packages.urllib3.disable_warnings()

FW_IP = sys.argv[1]
API_KEY = sys.argv[2] 

url = f"https://{FW_IP}/api/?type=op&cmd=<show><global-protect-gateway><statistics></statistics></global-protect-gateway></show>&key={API_KEY}"

try:
    resp = requests.get(url, verify=False, timeout=15)
    root = ET.fromstring(resp.text)
    
    zabbix_data = []
    for gateway in root.findall('.//gateway'):
        gw_name = gateway.find('name').text
        active_users = gateway.find('CurrentUsers').text
        zabbix_data.append({
            "{#GATEWAY_NAME}": gw_name,
            "active_users": int(active_users)
        })
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))