#!/bin/bash
# Executar no servidor slave. Requer permissão no pg_hba.conf para o usuário Zabbix.
psql -U postgres -t -c "SELECT COALESCE(EXTRACT(EPOCH FROM (now() - pg_last_xact_replay_timestamp())), 0);" | tr -d ' '