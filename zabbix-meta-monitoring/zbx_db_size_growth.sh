#!/bin/bash
psql -U zabbix -t -c "SELECT pg_database_size('zabbix');" | tr -d ' '