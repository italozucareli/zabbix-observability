#!/usr/bin/env python3
import subprocess, json

try:
    cmd = ["docker", "node", "ls", "--format", "{{json .}}"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)

    zabbix_data = []
    for line in result.stdout.strip().split('\n'):
        if not line:
            continue
            
        node = json.loads(line)
        
        zabbix_data.append({
            "{#NODE_NAME}": node.get('Hostname', 'unknown'),
            "{#ENGINE_VERSION}": node.get('EngineVersion', 'unknown'),
            "{#NODE_ID}": node.get('ID', 'unknown')
        })

    print(json.dumps({"data": zabbix_data}, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))