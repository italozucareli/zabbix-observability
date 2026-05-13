#!/usr/bin/env python3
import os, json
DB_PATH = "/var/lib/grafana/grafana.db" # Executar via Zabbix Agent no servidor do Grafana
try:
    print(json.dumps({"sqlite_size_mb": round(os.path.getsize(DB_PATH) / (1024 * 1024), 2)}))
except Exception as e: print(json.dumps({"error": str(e)}))