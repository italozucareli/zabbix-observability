#!/usr/bin/env python3
import subprocess, json, sys

if len(sys.argv) < 2:
    print(json.dumps({"error": "Forneça o nome do UPS. Ex: ./zbx_nut_ups_stats.py myups"}))
    sys.exit(1)

ups_name = sys.argv[1]

try:
    output = subprocess.check_output(['upsc', ups_name], stderr=subprocess.STDOUT).decode('utf-8')
    
    ups_data = {}
    for line in output.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            # Substitui pontos por underscores na chave para facilitar o JSONPath no Zabbix
            safe_key = key.strip().replace('.', '_')
            val = value.strip()
            
            try:
                ups_data[safe_key] = float(val) if '.' in val else int(val)
            except ValueError:
                ups_data[safe_key] = val
                
    print(json.dumps(ups_data, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))