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
        
        # Define se é Manager ou Worker
        role = "Manager" if node.get('ManagerStatus') else "Worker"
        
        # Códigos de status para facilitar triggers no Zabbix (1 = OK, 0 = Falha)
        status_code = 1 if node.get('Status') == "Ready" else 0
        avail_code = 1 if node.get('Availability') == "Active" else 0

        zabbix_data.append({
            "{#NODE_NAME}": node.get('Hostname', 'unknown'),
            "{#NODE_ROLE}": role,
            "status_ready": status_code,
            "availability_active": avail_code
        })

    print(json.dumps({"data": zabbix_data}, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))