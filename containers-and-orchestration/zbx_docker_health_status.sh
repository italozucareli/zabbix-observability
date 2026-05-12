#!/bin/bash
# Retorna 'healthy', 'unhealthy' ou 'starting'
docker inspect --format='{{json .State.Health.Status}}' $1 | tr -d '"'