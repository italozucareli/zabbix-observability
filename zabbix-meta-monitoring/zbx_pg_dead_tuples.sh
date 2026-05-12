#!/bin/bash
psql -U zabbix -d zabbix -t -c "
SELECT relname, n_dead_tup, n_live_tup 
FROM pg_stat_user_tables 
WHERE relname IN ('history', 'history_uint', 'history_str', 'trends', 'trends_uint', 'events', 'alerts');" | awk -F'|' '
BEGIN { print "{\"data\":[" }
NF==3 {
    gsub(/ /, "", $1); gsub(/ /, "", $2); gsub(/ /, "", $3);
    if ($3 == 0) { bloat_pct = 0 } else { bloat_pct = ($2 / ($2 + $3)) * 100 }
    
    printf "%s{\"{#TABLE_NAME}\":\"%s\", \"dead_tuples\":%s, \"bloat_percent\":%.2f}", sep, $1, $2, bloat_pct; 
    sep=","
}
END { print "]}" }'