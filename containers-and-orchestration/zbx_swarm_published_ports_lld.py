#!/usr/bin/env python3
import subprocess, json

try:
    cmd = ["docker", "service", "ls", "--format", "{{json .}}"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    
    zabbix_data = []
    for line in result.stdout.strip().split('\n'):
        if not line: continue
        svc = json.loads(line)
        ports = svc.get('Ports', '')
        
        if ports:
            # O formato no CLI é "*:8080->80/tcp"
            for p in ports.split(','):
                if ':' in p and '->' in p:
                    pub_port = p.split(':')[1].split('->')[0]
                    zabbix_data.append({
                        "{#SERVICE_NAME}": svc['Name'],
                        "{#PUBLISHED_PORT}": pub_port
                    })
                    
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))