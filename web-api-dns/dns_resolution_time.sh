#!/bin/bash
# Uso: ./dns_resolution_time.sh <IP_SERVIDOR_DNS> <DOMINIO_PARA_TESTAR>
dig @$1 $2 | grep "Query time" | awk '{print $4}'