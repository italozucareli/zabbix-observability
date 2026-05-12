#!/bin/bash
redis-cli info keyspace | grep "^db" | awk -F'[:,=]' '
BEGIN { print "{\"data\":[" }
{
    printf "%s{\"{#DB_NAME}\":\"%s\", \"keys\":%s}", sep, $1, $3; sep=","
}
END { print "]}" }'