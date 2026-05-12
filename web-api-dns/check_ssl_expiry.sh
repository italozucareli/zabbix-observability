#!/bin/bash
# Uso: ./check_ssl_expiry.sh dominio.com.br
DOMAIN=$1
PORT=443
EXP_DATE=$(echo | openssl s_client -servername "$DOMAIN" -connect "$DOMAIN":"$PORT" 2>/dev/null | openssl x509 -noout -dates | grep notAfter | cut -d= -f2)
EXP_SEC=$(date -d "$EXP_DATE" +%s)
NOW_SEC=$(date +%s)
DAYS_LEFT=$(( (EXP_SEC - NOW_SEC) / 86400 ))
echo $DAYS_LEFT