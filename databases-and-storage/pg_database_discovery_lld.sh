#!/bin/bash
psql -U postgres -t -c "SELECT datname, pg_database_size(datname) FROM pg_database WHERE datistemplate = false;" | awk -F'|' '
BEGIN { print "{\"data\":[" }
NF==2 {
    gsub(/ /, "", $1); gsub(/ /, "", $2);
    printf "%s{\"{#DB_NAME}\":\"%s\", \"size_bytes\":%s}", sep, $1, $2; sep=","
}
END { print "]}" }'