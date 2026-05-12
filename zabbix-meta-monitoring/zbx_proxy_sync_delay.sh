#!/bin/bash
psql -U zabbix -d zabbix -t -c "
SELECT host, EXTRACT(EPOCH FROM now()) - lastaccess AS delay 
FROM hosts WHERE status = 5;" | awk -F'|' '
BEGIN { print "{\"data\":[" }
NF==2 {
    gsub(/^ +| +$/, "", $1);
    gsub(/ /, "", $2);
    printf "%s{\"{#PROXY_NAME}\":\"%s\", \"delay_seconds\":%s}", sep, $1, $2; sep=","
}
END { print "]}" }'