#!/usr/bin/env python3
import json, sys, os
from collections import Counter

log_file = "/var/log/zabbix/zabbix_server.log"
if not os.path.exists(log_file):
    print(json.dumps({"error": "Log file not found"}))
    sys.exit(1)

categories = {
    "db_down": 0,
    "poller_busy": 0,
    "unreachable_hosts": 0,
    "network_error": 0,
    "oom_killer": 0
}

try:
    with os.popen(f"tail -n 1000 {log_file}") as f:
        for line in f:
            line_lower = line.lower()
            if "database is down" in line_lower or "connection to database" in line_lower:
                categories["db_down"] += 1
            elif "more than 75% busy" in line_lower:
                categories["poller_busy"] += 1
            elif "temporarily disabling" in line_lower or "unreachable" in line_lower:
                categories["unreachable_hosts"] += 1
            elif "network error" in line_lower or "timed out" in line_lower:
                categories["network_error"] += 1
            elif "out of memory" in line_lower:
                categories["oom_killer"] += 1

    print(json.dumps(categories))
except Exception as e:
    print(json.dumps({"error": str(e)}))