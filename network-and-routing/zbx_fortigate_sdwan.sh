#!/bin/bash
# Uso: ./zbx_fortigate_sdwan.sh <IP> <API_TOKEN>
FGT_IP=$1
TOKEN=$2

curl -s -k -H "Authorization: Bearer $TOKEN" "https://$FGT_IP/api/v2/monitor/virtual-wan/health-check" | jq '
{
  data: [
    .results[] | {
      "{#HEALTH_CHECK_NAME}": .name,
      "{#MEMBER_NAME}": .members[].name,
      "latency": .members[].latency,
      "jitter": .members[].jitter,
      "packet_loss": .members[].packet_loss,
      "state": .members[].state
    }
  ]
}'