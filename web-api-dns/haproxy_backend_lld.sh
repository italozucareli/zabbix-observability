#!/bin/bash
echo "show stat" | socat unix-connect:/var/run/haproxy.sock stdio | awk -F',' '
BEGIN { print "{\"data\":[" }
$1 != "# pxname" && $2 != "FRONTEND" && $2 != "BACKEND" && NF>0 {
    printf "%s{\"{#BACKEND}\":\"%s\", \"{#SERVER}\":\"%s\", \"status\":\"%s\"}", sep, $1, $2, $18; sep=","
}
END { print "]}" }'