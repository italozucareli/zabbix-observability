#!/bin/bash
curl -s http://localhost/upstream_conf | awk '
BEGIN { print "{\"data\":[" }
/^upstream/ {
    printf "%s{\"{#UPSTREAM_NAME}\":\"%s\"}", sep, $2; sep=","
}
END { print "]}" }'