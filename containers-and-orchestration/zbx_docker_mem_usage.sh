#!/bin/bash
docker stats --no-stream --format "{{.MemUsage}}" $1 | awk '{print $1}' | sed 's/MiB//'