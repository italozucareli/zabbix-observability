#!/usr/bin/env python3
import json, subprocess
result = subprocess.run(['curl', '-s', '--unix-socket', '/var/run/docker.sock', 'http://localhost/containers/json?all=true'], stdout=subprocess.PIPE)
containers = json.loads(result.stdout)
zabbix_data = []
for c in containers:
    zabbix_data.append({
        "{#CONTAINER_ID}": c['Id'][:12],
        "{#CONTAINER_NAME}": c['Names'][0].strip('/'),
        "state": c['State'],
        "status": c['Status']
    })
print(json.dumps({"data": zabbix_data}))