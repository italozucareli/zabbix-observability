#!/bin/bash
# Executar via Zabbix Agent em qualquer nó (Manager ou Worker)
docker volume ls -qf dangling=true 2>/dev/null | wc -l || echo 0