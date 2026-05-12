#!/bin/bash
echo '{"data":['
first=1
for iface in $(ls /sys/class/net/); do
    [ $first -eq 0 ] && echo "," || first=0
    rx=$(cat /sys/class/net/$iface/statistics/rx_bytes)
    tx=$(cat /sys/class/net/$iface/statistics/tx_bytes)
    oper=$(cat /sys/class/net/$iface/operstate 2>/dev/null || echo "unknown")
    echo "{\"{#IFNAME}\":\"$iface\", \"rx_bytes\":$rx, \"tx_bytes\":$tx, \"operstate\":\"$oper\"}"
done
echo ']}'