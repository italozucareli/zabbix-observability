#!/bin/bash
HOST=$1
USER=$2
PASS=$3
curl -s -u "$USER:$PASS" "http://$HOST:15672/api/queues" | jq '{data: [ .[] | { "{#VHOST}": .vhost, "{#QUEUE_NAME}": .name, "messages": .messages, "messages_unacknowledged": .messages_unacknowledged } ] }'