#!/bin/bash
lsblk -nd -o NAME,TYPE | awk '$2=="disk" {print $1}' | awk '
BEGIN { print "{\"data\":[" }
{
    printf "%s{\"{#DISK_NAME}\":\"%s\"}", sep, $1; sep=","
}
END { print "]}" }'