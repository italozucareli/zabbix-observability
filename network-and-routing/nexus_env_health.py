#!/usr/bin/env python3
# Uso: ./nexus_env_health.py <IP> <USER> <PASS>
import requests, sys, json
requests.packages.urllib3.disable_warnings()

if len(sys.argv) != 4:
    print("0")
    sys.exit()

url = f"http://{sys.argv[1]}/ins"
payload = {
    "ins_api": {
        "version": "1.0", "type": "cli_show", "chunk": "0", "sid": "1",
        "input": "show system resources", "output_format": "json"
    }
}
try:
    response = requests.post(url, auth=(sys.argv[2], sys.argv[3]), json=payload, verify=False, timeout=10)
    data = response.json()
    # Retorna o uso de CPU (user + kernel)
    cpu_user = float(data['ins_api']['outputs']['output']['body']['cpu_state_user'])
    cpu_kernel = float(data['ins_api']['outputs']['output']['body']['cpu_state_kernel'])
    print(cpu_user + cpu_kernel)
except:
    print("-1")