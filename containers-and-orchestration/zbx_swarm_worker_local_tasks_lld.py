#!/usr/bin/env python3
import subprocess, json

try:
    cmd = ["docker", "ps", "--format", "{{json .}}"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    
    zabbix_data = []
    for line in result.stdout.strip().split('\n'):
        if not line: continue
        container = json.loads(line)
        labels = container.get('Labels', '')
        
        # Swarm injeta automaticamente a label com o nome do serviço
        svc_name = None
        for label in labels.split(','):
            if label.startswith('com.docker.swarm.service.name='):
                svc_name = label.split('=')[1]
                break
                
        if svc_name:
            zabbix_data.append({
                "{#SERVICE_NAME}": svc_name,
                "{#CONTAINER_ID}": container['ID'],
                "{#CONTAINER_NAME}": container['Names']
            })
            
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))