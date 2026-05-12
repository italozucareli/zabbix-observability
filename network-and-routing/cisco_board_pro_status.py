#!/usr/bin/env python3
# Uso: ./cisco_board_pro_status.py <IP> <USER> <PASS>
import requests, sys
requests.packages.urllib3.disable_warnings()

try:
    url = f"https://{sys.argv[1]}/putxml"
    headers = {"Content-Type": "text/xml"}
    xml = '<Configuration><Standby><State>Get</State></Standby></Configuration>'
    response = requests.post(url, auth=(sys.argv[2], sys.argv[3]), data=xml, verify=False, timeout=5)
    if "Standby" in response.text:
        print("1") # Acessível e respondendo
    else:
        print("0")
except:
    print("0")