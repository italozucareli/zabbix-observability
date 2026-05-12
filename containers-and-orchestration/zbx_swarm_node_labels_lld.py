#!/usr/bin/env python3
import subprocess, json

try:
    nodes_out = subprocess.run(["docker", "node", "ls", "-q"], capture_output=True, text=True, check=True)
    nodes = nodes_out.stdout.strip().split('\n')
    
    zabbix_data = []
    for node in nodes:
        if not node: continue
        insp = subprocess.run(["docker", "node", "inspect", node], capture_output=True, text=True)
        data = json.loads(insp.stdout)[0]
        
        hostname = data['Description']['Hostname']
        labels = data['Spec'].get('Labels', {})
        
        for key, val in labels.items():
            zabbix_data.append({
                "{#NODE_HOSTNAME}": hostname,
                "{#LABEL_KEY}": key,
                "{#LABEL_VALUE}": val
            })
            
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))