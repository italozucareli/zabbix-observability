#!/usr/bin/env python3
import json, sys
log_file = sys.argv[1]
clients = []
with open(log_file, 'r') as f:
    start_parsing = False
    for line in f.readlines():
        if "ROUTING TABLE" in line: break
        if start_parsing:
            parts = line.strip().split(',')
            if len(parts) >= 5:
                clients.append({
                    "{#CLIENT_NAME}": parts[0],
                    "real_ip": parts[1].split(':')[0],
                    "bytes_recv": parts[2],
                    "bytes_sent": parts[3]
                })
        if "Connected Since" in line: start_parsing = True
print(json.dumps({"data": clients}))