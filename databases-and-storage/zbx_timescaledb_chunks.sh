#!/bin/bash
psql -U zabbix -t -c "
SELECT hypertable_name, COUNT(chunk_name) 
FROM timescaledb_information.chunks 
WHERE hypertable_name IN ('history', 'history_uint', 'trends', 'trends_uint') 
GROUP BY hypertable_name;" | awk -F'|' '
BEGIN { print "{\"data\":[" }
NF==2 {
    gsub(/ /, "", $1); gsub(/ /, "", $2);
    printf "%s{\"{#TABLE_NAME}\":\"%s\", \"chunks_count\":%s}", sep, $1, $2; sep=","
}
END { print "]}" }'