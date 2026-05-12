#!/bin/bash
zpool list -H -o name,health,capacity | awk '
BEGIN { print "{\"data\":[" }
{
    printf "%s{\"{#POOL_NAME}\":\"%s\", \"health\":\"%s\", \"capacity\":\"%s\"}", sep, $1, $2, $3; sep=","
}
END { print "]}" }'