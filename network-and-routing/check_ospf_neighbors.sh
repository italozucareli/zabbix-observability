#!/bin/bash
# Uso: ./check_ospf_neighbors.sh <IP_ROTEADOR> <COMUNIDADE_SNMP> <IP_NEIGHBOR>
HOST=$1
COMMUNITY=$2
NEIGHBOR=$3
# OID para ospfNbrState
snmpwalk -v2c -c "$COMMUNITY" "$HOST" 1.3.6.1.2.1.14.10.1.6."$NEIGHBOR".0 | awk '{print $NF}'