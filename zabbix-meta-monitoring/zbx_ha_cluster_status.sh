#!/bin/bash
psql -U zabbix -d zabbix -t -c "
SELECT name, status, EXTRACT(EPOCH FROM now()) - lastaccess AS lag_seconds 
FROM ha_node;" | awk -F'|' '
BEGIN { print "{\"data\":[" }
NF>=3 {
    gsub(/^ +| +$/, "", $1); 
    gsub(/ /, "", $2);       
    gsub(/ /, "", $3);       
    
    printf "%s{\"{#NODE_NAME}\":\"%s\", \"status\":%s, \"lag_seconds\":%s}", sep, $1, $2, $3; 
    sep=","
}
END { print "]}" }'