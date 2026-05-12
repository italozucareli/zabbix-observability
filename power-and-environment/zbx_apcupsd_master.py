#!/usr/bin/env python3
import subprocess, json, sys

try:
    # Executa o apcaccess em modo unformatted (-u)
    output = subprocess.check_output(['apcaccess', '-u'], stderr=subprocess.STDOUT).decode('utf-8')
    
    ups_data = {}
    for line in output.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            # Remove espaços em branco
            key = key.strip()
            value = value.strip()
            
            # Tenta converter valores numéricos para facilitar as triggers no Zabbix
            try:
                if '.' in value:
                    ups_data[key] = float(value)
                else:
                    ups_data[key] = int(value)
            except ValueError:
                ups_data[key] = value
                
    print(json.dumps(ups_data, indent=2))
except subprocess.CalledProcessError as e:
    print(json.dumps({"error": f"apcaccess failed: {e.output.decode('utf-8').strip()}"}))
except Exception as e:
    print(json.dumps({"error": str(e)}))