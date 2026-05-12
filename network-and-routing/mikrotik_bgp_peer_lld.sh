#!/bin/bash
ROUTER_IP=$1
USER=$2
PASS=$3
curl -k -u "$USER:$PASS" "https://$ROUTER_IP/rest/routing/bgp/session" | jq '{data: [ .[] | { "{#PEER_NAME}": .name, "{#REMOTE_AS}": ."remote.as", "state": .state, "uptime": .uptime } ] }'