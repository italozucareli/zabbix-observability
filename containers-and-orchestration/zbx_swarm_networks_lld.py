#!/usr/bin/env python3
import subprocess, json

try:
    # Filtra apenas redes gerenciadas pelo Swarm (scope = swarm)
    cmd = ["docker", "network", "ls", "--filter", "scope=swarm", "--format", "{{json .}}"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)

    zabbix_data = []
    for line in result.stdout.strip().split('\n'):
        if not line:
            continue
            
        net = json.loads(line)
        
        zabbix_data.append({
            "{#NETWORK_NAME}": net.get('Name', 'unknown'),
            "{#NETWORK_ID}": net.get('ID', 'unknown'),
            "{#NETWORK_DRIVER}": net.get('Driver', 'unknown')
        })

    print(json.dumps({"data": zabbix_data}, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))