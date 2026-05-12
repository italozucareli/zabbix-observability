#!/bin/bash
psql -U zabbix -d zabbix -t -c "
SELECT 
  (SELECT count(*) FROM items WHERE state=1 AND status=0) AS unsupported_items,
  (SELECT count(*) FROM hosts WHERE status=1) AS disabled_hosts,
  (SELECT count(*) FROM triggers WHERE state=1) AS unsupported_triggers;" | awk -F'|' '
{
    gsub(/ /, "", $1); gsub(/ /, "", $2); gsub(/ /, "", $3);
    if ($1 != "") {
        printf "{\"unsupported_items\":%s, \"disabled_hosts\":%s, \"unsupported_triggers\":%s}\n", $1, $2, $3
    }
}'