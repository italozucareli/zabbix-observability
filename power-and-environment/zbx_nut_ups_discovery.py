#!/usr/bin/env python3
import subprocess, json

try:
    # Lista os nomes dos UPS configurados no NUT
    output = subprocess.check_output(['upsc', '-l'], stderr=subprocess.STDOUT).decode('utf-8')
    ups_list = [line.strip() for line in output.split('\n') if line.strip()]
    
    zabbix_data = []
    for ups in ups_list:
        zabbix_data.append({
            "{#UPS_NAME}": ups
        })
        
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))