#!/bin/bash
# Uso: ./vpn_ipsec_tunnel.sh <IP_DESTINO_VIA_TUNEL>
IP=$1
ping -c 3 -W 2 "$IP" > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo 1 # UP
else
    echo 0 # DOWN
fi