#!/bin/bash
HOST=$1
curl -s "http://$HOST:9200/_cat/indices?format=json" | jq '{data: [ .[] | { "{#INDEX_NAME}": .index, "health": .health, "status": .status, "store_size": .["store.size"] } ] }'