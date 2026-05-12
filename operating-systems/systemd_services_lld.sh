#!/bin/bash
systemctl list-unit-files --type=service --state=enabled --no-pager | awk '
BEGIN { print "{\"data\":[" }
/enabled/ {
    name = $1; sub(/\.service$/, "", name);
    printf "%s{\"{#SERVICE_NAME}\":\"%s\"}", sep, name; sep=","
}
END { print "]}" }'