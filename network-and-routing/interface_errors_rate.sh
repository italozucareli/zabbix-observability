#!/bin/bash
# Uso: ./interface_errors_rate.sh <INTERFACE_NAME> (ex: eth0)
IFACE=$1
if [ -f "/sys/class/net/$IFACE/statistics/rx_errors" ]; then
    cat /sys/class/net/$IFACE/statistics/rx_errors
else
    echo "-1"
fi