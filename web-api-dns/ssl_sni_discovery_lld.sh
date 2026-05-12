#!/bin/bash
grep -r "server_name" /etc/nginx/sites-enabled/ | awk '{print $3}' | tr -d ';' | sort -u | awk '
BEGIN { print "{\"data\":[" }
{
    printf "%s{\"{#DOMAIN_NAME}\":\"%s\"}", sep, $1; sep=","
}
END { print "]}" }'