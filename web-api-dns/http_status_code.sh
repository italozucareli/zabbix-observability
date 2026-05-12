#!/bin/bash
# Uso: ./http_status_code.sh https://meusite.com
curl -s -o /dev/null -w "%{http_code}" -m 10 "$1"