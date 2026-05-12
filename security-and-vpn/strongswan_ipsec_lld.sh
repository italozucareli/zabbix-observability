#!/bin/bash
ipsec statusall | awk '
BEGIN { print "{\"data\":[" }
/Connections:/ { flag=1; next }
/Security Associations:/ { flag=0 }
flag && /^[a-zA-Z0-9_-]+:/ {
    name = $1; sub(/:/, "", name);
    printf "%s{\"{#TUNNEL_NAME}\":\"%s\"}", sep, name; sep=","
}
END { print "]}" }'