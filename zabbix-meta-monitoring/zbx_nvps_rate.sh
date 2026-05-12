#!/bin/bash
psql -U zabbix -t -c "SELECT count(*)/60 FROM history WHERE clock > (extract(epoch from now()) - 60);" | tr -d ' '