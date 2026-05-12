#!/bin/bash
# Uso: ./check_bgp_peers.sh <IP_ROTEADOR> <COMUNIDADE_SNMP> <IP_PEER_BGP>
HOST=$1
COMMUNITY=$2
PEER=$3
# OID para cbgpPeerState
snmpwalk -v2c -c "$COMMUNITY" "$HOST" 1.3.6.1.4.1.9.9.187.1.2.5.1.3."$PEER" | awk '{print $NF}'