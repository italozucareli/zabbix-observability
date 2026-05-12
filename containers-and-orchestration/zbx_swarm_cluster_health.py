#!/usr/bin/env python3
import subprocess, json

try:
    cmd = ["docker", "info", "--format", "{{json .Swarm}}"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    swarm_info = json.loads(result.stdout.strip())
    
    # 1 = Active/True, 0 = Inactive/False/Error
    local_state = 1 if swarm_info.get('LocalNodeState') == 'active' else 0
    control_available = 1 if swarm_info.get('ControlAvailable') else 0
    
    zabbix_data = {
        "local_node_state": local_state,
        "control_available": control_available,
        "managers_count": swarm_info.get('Managers', 0),
        "nodes_count": swarm_info.get('Nodes', 0),
        "error": swarm_info.get('Error', '')
    }
    
    print(json.dumps(zabbix_data, indent=2))
except subprocess.CalledProcessError as e:
    print(json.dumps({"error": f"Command failed: {e.stderr}"}))
except Exception as e:
    print(json.dumps({"error": str(e)}))