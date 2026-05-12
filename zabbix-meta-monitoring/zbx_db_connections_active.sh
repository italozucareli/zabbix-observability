#!/bin/bash
psql -U zabbix -t -c "SELECT count(*) FROM pg_stat_activity WHERE datname='zabbix' AND state='active';" | tr -d ' '