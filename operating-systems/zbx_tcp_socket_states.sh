#!/bin/bash
ss -ant | awk 'NR>1 {print $1}' | sort | uniq -c | awk '
BEGIN { print "{\"data\":[" }
{
    printf "%s{\"{#TCP_STATE}\":\"%s\", \"count\":%s}", sep, $2, $1; sep=","
}
END { print "]}" }'