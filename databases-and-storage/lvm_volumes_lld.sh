#!/bin/bash
lvs --noheadings -o lv_name,vg_name,data_percent | awk '
BEGIN { print "{\"data\":[" }
{
    printf "%s{\"{#LV_NAME}\":\"%s\", \"{#VG_NAME}\":\"%s\", \"data_percent\":\"%s\"}", sep, $1, $2, $3; sep=","
}
END { print "]}" }'