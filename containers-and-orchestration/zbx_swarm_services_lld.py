#!/usr/bin/env python3
import subprocess, json, sys

try:
    # Coleta a lista de serviços do Swarm em formato JSON
    cmd = ["docker", "service", "ls", "--format", "{{json .}}"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)

    zabbix_data = []
    for line in result.stdout.strip().split('\n'):
        if not line:
            continue
            
        svc = json.loads(line)
        
        # O Swarm nomeia os servicos como "NomeDaStack_NomeDoServico"
        name_parts = svc['Name'].split('_', 1)
        stack_name = name_parts[0] if len(name_parts) > 1 else "default_stack"
        svc_name = name_parts[1] if len(name_parts) > 1 else svc['Name']

        # O campo Replicas vem no formato "Running/Desired" (ex: "3/3")
        replicas_str = svc.get('Replicas', '0/0')
        running, desired = 0, 0
        if '/' in replicas_str:
            r_parts = replicas_str.split('/')
            running = int(r_parts[0])
            desired = int(r_parts[1])

        zabbix_data.append({
            "{#STACK_NAME}": stack_name,
            "{#SERVICE_NAME}": svc_name,
            "{#FULL_NAME}": svc['Name'],
            "replicas_running": running,
            "replicas_desired": desired,
            "mode": svc.get('Mode', 'unknown')
        })

    print(json.dumps({"data": zabbix_data}, indent=2))
except subprocess.CalledProcessError as e:
    print(json.dumps({"error": f"Erro ao executar docker service ls: {e.stderr}"}))
except Exception as e:
    print(json.dumps({"error": str(e)}))