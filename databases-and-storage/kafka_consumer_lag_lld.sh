#!/bin/bash
BOOTSTRAP_SERVER=$1
kafka-consumer-groups.sh --bootstrap-server "$BOOTSTRAP_SERVER" --describe --all-groups | awk '
BEGIN { print "{\"data\":[" }
NR>1 && NF>5 {
    printf "%s{\"{#GROUP}\":\"%s\", \"{#TOPIC}\":\"%s\", \"lag\":%s}", sep, $1, $2, $6; sep=","
}
END { print "]}" }'