#!/bin/bash
# Uso: ./check_domain_expiry.sh site.com.br
EXP_DATE=$(whois $1 | grep "expires:" | awk '{print $2}')
if [ -n "$EXP_DATE" ]; then
    EXP_SEC=$(date -d "$(echo $EXP_DATE | set -e; sed 's/\(........\)/\1/') " +%s)
    NOW_SEC=$(date +%s)
    echo $(( (EXP_SEC - NOW_SEC) / 86400 ))
else
    echo "-1"
fi