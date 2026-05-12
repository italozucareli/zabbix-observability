#!/bin/bash
curl -s -X GET "https://api.digitalocean.com/v2/droplets" -H "Authorization: Bearer $1" | jq '{data: [ .droplets[] | {"{#DROPLET_NAME}": .name, "status": .status} ]}'