#!/bin/bash
ss -ant | awk '$4 ~ /:10051$/ {print $1}' | sort | uniq -c | awk '
BEGIN { print "{\"data\":[" }
{
    printf "%s{\"{#TRAPPER_STATE}\":\"%s\", \"count\":%s}", sep, $2, $1; 
    sep=","
}
END { print "]}" }'