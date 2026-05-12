#!/bin/bash
psql -U zabbix -t -c "SELECT count(*) FROM items WHERE state=1 AND status=0;" | tr -d ' '