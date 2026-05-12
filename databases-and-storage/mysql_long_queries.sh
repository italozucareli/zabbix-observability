#!/bin/bash
# Requer .my.cnf configurado com credenciais para o usuário Zabbix
mysql -e "SHOW PROCESSLIST" | awk '$6 > 60 && $5 != "Sleep" {print $0}' | wc -l